
#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
AUTHORING = ROOT / "authoring"

def main():
    if not AUTHORING.exists():
        print("[WARN] Missing docs/authoring")
        return 0
    print("[OK] pipeline noop")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
