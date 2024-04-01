import utile.message
import utile.network as network
import utile.message as message
import utile.data as data
import utile.security as security
import threading
import queue
import string
import socket


LOCAL_IP = socket.gethostname()
PORT_SERV_CLES = 8380
def generate_key(longueur=0, caracteres=string.ascii_letters + string.digits):
    """
    Générer une clé de longueur (longueur) contenant uniquement les caractères (caracteres)
    :param longueur: La longueur de la clé à générer
    :param caracteres: Les caractères qui composeront la clé
    :return: La clé générée
    """


def main():
    server_socket = network.start_net_serv(LOCAL_IP, PORT_SERV_CLES)
      # Stocker la clé partagée
    # Boucle infinie pour accepter les connexions entrantes
    while True:
        # Accepter une nouvelle connexion
        client_socket, client_address = server_socket.accept()
        print(f"Connection établie avec {client_address}")
        shared_key = security.diffie_hellman_recv_key(client_socket)
        print()

        # Lire les messages reçus du client
        while True:
            # Recevoir des données du client
            datas = network.receive_message(client_socket)  # Utiliser la fonction receive_message du module network
            if not datas:
                # Si aucune donnée n'est reçue, cela signifie que le client a fermé la connexion
                print(f"Client {client_address} déconnecté")
                break
            # Afficher les données reçues
            print(f"Message reçu du client {client_address}: {datas}")
            # Chiffrer le message avec la clé partagée
            encrypted_message = security.aes_encrypt(datas, shared_key)
            # Envoyer le message chiffré
            network.send_message(client_socket, encrypted_message)
        # Fermer le socket client
        client_socket.close()

    exit(0)

if __name__ == '__main__':
    main()

