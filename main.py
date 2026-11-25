"""Write this entry's one line to the output directory.

Reads entry.txt next to this file and copies it verbatim to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output), mode 0644.
"""
import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_bytes()
    if not text.strip():
        raise ValueError("entry.txt is empty or whitespace only")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        pass
    target = out_dir / "entry.txt"
    target.write_bytes(text)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
