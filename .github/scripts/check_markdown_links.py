import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
FENCED_CODE = re.compile(r"(?ms)^(```+|~~~+).*?^\1[ \t]*$")
INLINE_CODE = re.compile(r"(`+).*?\1")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]+\]\(\s*(?:<([^>]+)>|([^\s)]+))[^)]*\)")


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts)
        and ".venv" not in path.parts
        and "node_modules" not in path.parts
    )


def check_links() -> list[str]:
    errors = []
    for markdown_file in markdown_files():
        content = markdown_file.read_text(encoding="utf-8")
        content = FENCED_CODE.sub("", content)
        content = INLINE_CODE.sub("", content)

        for match in MARKDOWN_LINK.finditer(content):
            target = match.group(1) or match.group(2)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue

            path = markdown_file.parent / unquote(parsed.path)
            if not path.exists():
                relative_file = markdown_file.relative_to(ROOT)
                errors.append(f"{relative_file}: broken link target {target!r}")

    return errors


if __name__ == "__main__":
    failures = check_links()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)

    print(f"Checked local Markdown links in {len(markdown_files())} files.")
