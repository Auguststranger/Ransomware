# import json
import pickle
import socket
import time

# Constantes
HEADERSIZE = 10
LOCAL_IP = socket.gethostname()
PORT_SERV_CLES = 8380


def start_net_serv(ip=LOCAL_IP, port=PORT_SERV_CLES):
    """
    Démarre un socket qui écoute en mode "serveur" sur ip:port
    :param ip: l'adresse ip à utiliser
    :param port: le port à utilier
    :return: le socket créé en mode "serveur"
    """

    try:
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the IP address and port
        server_socket.bind((ip, port))

        # Start listening for incoming connections
        server_socket.listen()
        print(f"Server listening on {ip}:{port}")
        return server_socket
    except ConnectionError:
        print("Connexion error")
        return None


def connect_to_serv(ip=LOCAL_IP, port=PORT_SERV_CLES, retry=0):
    """
    Crée un socket qui tente de se connecter sur ip:port.
    En cas d'échec, tente une nouvelle connexion après retry secondes
    :param ip: l'adresse ip où se connecter
    :param port: le port de connexion
    :param retry: le nombre de seconde à attendre avant de tenter une nouvelle connexion
    :return: le socket créé en mode "client"
    """

    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, port))
            print(f"Connected to server at {ip}:{port}")
        except ConnectionRefusedError:
            print(f"Connection to {ip}:{port} refused. Retrying in {retry} seconds...")
            time.sleep(retry)
        else:
            return client_socket


def send_message(s, msg=b''):
    """
    Envoi un message sur le réseau
    :param s: (socket) pour envoyer le message
    :param msg: (dictionary) message à envoyer
    :return: Néant
    """

    data = pickle.dumps(msg)
    try:
        header = bytes(f"{len(data):<{HEADERSIZE}}", "utf-8")
        mesg = (header + data)
        s.sendall(mesg)
    except ConnectionResetError:
        print("La connexion a été fermée")


def receive_message(s):
    """
    Réceptionne un message sur le réseau
    :param s: (socket) pour réceptionner le message
    :return: (objet) réceptionné
    """
    try:
        # Recevoir la taille du message
        head = int(s.recv(HEADERSIZE))
        # Recevoir le message complet
        datas = s.recv(head)
        while len(datas) < head:
            packet = s.recv(head - len(datas))
            if not packet:
                break
            datas += packet
        return pickle.loads(datas)
    except ConnectionResetError:
        print("La connexion a été fermée")

