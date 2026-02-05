# Task 2 – Analyse de logs
# TODO : lire un fichier log.txt et compter les lignes et erreurs

from pathlib import Path

LOG_FILE = Path("log.txt")


def analyze_logs(path):
    path = Path(path)
    lines = path.read_text().splitlines()
    total = len(lines)
    errors = sum(1 for line in lines if line.startswith("ERROR"))
    return total, errors


def main():
    if not LOG_FILE.exists():
        print("Fichier log.txt non trouvé")
        return

    total, errors = analyze_logs(LOG_FILE)
    print(f"Nombre de lignes : {total}")
    print(f"Nombre d'erreurs : {errors}")


if __name__ == "__main__":
    main()
