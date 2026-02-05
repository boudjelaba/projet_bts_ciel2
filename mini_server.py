# BONUS – Mini serveur HTTP
# TODO : simple serveur HTTP pour afficher "Hello World"

from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8000


def main():
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serveur HTTP démarré sur http://localhost:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur...")
        server.server_close()


if __name__ == "__main__":
    main()
