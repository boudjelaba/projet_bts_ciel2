# Task 3 – Test réseau
# TODO : tester si un hôte est accessible

import subprocess
import platform


def ping(host: str) -> bool:
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


def main():
    host = input("Entrez l'adresse IP ou le nom d'hôte : ").strip()

    if not host:
        print("Adresse invalide")
        return

    if ping(host):
        print(f"{host} est accessible")
    else:
        print(f"{host} n'est pas accessible")


if __name__ == "__main__":
    main()
