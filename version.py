from pathlib import Path

VERSION_FILE = Path(__file__).parent / "VERSION"


def get_version() -> str:
    try:
        return VERSION_FILE.read_text().strip()
    except FileNotFoundError:
        return "0.0.0"
