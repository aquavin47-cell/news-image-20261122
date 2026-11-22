"""Sum up 22 November 2026 world news in one image.

Deterministic, no network: copies the bundled news.png to
/output/entry.png (or to the path in ENTRY_OUTPUT, for local testing).
Running it twice writes the same bytes.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news.png"
OUTPUT = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.png"))


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # Verify the copy is byte-complete before reporting success.
    if OUTPUT.stat().st_size != SOURCE.stat().st_size:
        print("copy incomplete", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
