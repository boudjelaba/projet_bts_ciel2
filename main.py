# Task 1 – Python : prise en main
# TODO : compléter le code pour afficher un message personnalisé

from version import get_version


def main():
    name = input("Quel est ton prénom ? ").strip()
    if not name:
        name = "utilisateur"

    version = get_version()

    print(f"Bonjour {name}, bienvenue dans le projet BTS CIEL !")
    print(f"Version du projet : {version}")


if __name__ == "__main__":
    main()
