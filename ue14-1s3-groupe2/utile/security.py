import hashlib

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import getPrime
from random import randint
from hashlib import sha256
import utile.network as network
import pickle
from Crypto.Util import number


def aes_encrypt(msg, shared_key):
    """
    Fonction de chiffrement AES-GCM
    :param msg: (dict) Message au format de dictionnaire à chiffrer
    :param shared_key: (bytes) Clé partagée pour le chiffrement
    :return: (list) Liste des éléments nécessaires au déchiffrement --> [nonce, ciphertext, tag]
    """
    # Vérifier si le message est déjà sérialisé
    serialized_msg = msg if isinstance(msg, bytes) else pickle.dumps(msg)

    # initialiser le chiffreur AES en mode GCM avec la clé partagée
    cipher = AES.new(shared_key, AES.MODE_GCM)

    # chiffrer le message
    ciphertext, tag = cipher.encrypt_and_digest(serialized_msg)

    # récupérer la nonce utilisée pour le chiffrement
    nonce = cipher.nonce

    # retourner les éléments nécessaires au déchiffrement
    return [nonce, ciphertext, tag]


def aes_decrypt(msg, shared_key):
    """
    Fonction de déchiffrement AES-GCM
    :param msg: (list) Liste des éléments nécessaires au déchiffrement --> [nonce, ciphertext, tag]
    :param shared_key: (bytes) Clé partagée pour le déchiffrement
    :return: (dict) Message déchiffré sous forme de dictionnaire
    """
    nonce, ciphertext, tag = msg  # extraire nonce, ciphertext, et tag de la liste d'entrée

    # initialiser le déchiffreur AES en mode GCM avec la clé partagée et le nonce
    cipher = AES.new(shared_key, AES.MODE_GCM, nonce=nonce)

    # déchiffrer et vérifier l'intégrité du message
    try:
        serialized_msg = cipher.decrypt_and_verify(ciphertext, tag)
        # désérialiser les données déchiffrées en dictionnaire
        return pickle.loads(serialized_msg)
    except (ValueError, KeyError) as e:
        print(f'erreur lors du déchiffrement : {e}')
        return None

def gen_key(size=256):
    """
    Fonction générant une clé de chiffrement
    :param size: (bits) taille de la clé à générer
    :return: (bytes) nouvelle clé de chiffrement
    """
    # je verifie que la taille spécifie est un multiple de 8
    if size % 8 != 0:
        raise ValueError("la taille de le clé est un multiple de 8")
    # convertir la taille de la clé en bits en octets
    size_bytes = size // 8

    # génère et retourne la clé
    return get_random_bytes(size_bytes)

def diffie_hellman_send_key(s_client):
    try:
        # Génération de nombre premier P et générateur G
        P = getPrime(2048)
        G = randint(2, P - 1)

        # Génération de clé privée et de clé publique
        private_key = randint(2, P - 1)
        public_key = G ** private_key % P

        # Envoyer P, G et la clé publique au serveur
        message = {
            'P': P,
            'G': G,
            'public_key': public_key
        }
        network.send_message(s_client, message)

        # Recevoir P et la clé publique du serveur
        response = network.receive_message(s_client)
        P_server = response['P_server']
        public_key_server = response['public_key_client']

        # Vérifier si les valeurs de P reçues correspondent à la valeur initiale
        if P != P_server:
            raise ValueError("Les valeurs de P reçues ne correspondent pas")

        # Calcul de la clé partagée
        shared_key = public_key_server** private_key% P

        return shared_key
    except Exception as e:
        print(f"Erreur lors de l'envoi de la clé partagée : {e}")
        return None


def diffie_hellman_recv_key(s_serveur):
    try:
        # Recevoir le message complet du client
        message = network.receive_message(s_serveur)

        # Extraire les valeurs nécessaires du message reçu
        P_client = message['P_client']
        G_client = message['G_client']
        public_key_client = message['public_key_client']

        # Génération de clé privée et de clé publique
        private_key = randint(2, P_client - 1)
        public_key_server = G_client** private_key% P_client

        # Rassembler les données à envoyer dans un dictionnaire
        message = {
            'P_client': P_client,
            'G_client': G_client,
            'public_key_server': public_key_server
        }

        # Envoyer le message au client
        network.send_message(s_serveur, message)

        # Calcul de la clé partagée
        shared_key = public_key_client ** private_key % P_client

        return shared_key
    except Exception as e:
        print(f"Erreur lors de la réception de la clé partagée : {e}")
        return None
