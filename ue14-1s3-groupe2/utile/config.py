import json
import utile.security as security
import pickle
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
from cryptography.fernet import Fernet
from security import aes_encrypt,aes_decrypt,gen_key

loaded_config ={}

def load_config(config_file='config/config.cfg', key_file='config/key.bin'):
    """
    Fonction permettant de charger la configuration au format JSON avec cryptage AES-GCM
    :param config_file: (str) Fichier d'enregistrement de la configuration
    :param key_file: (str) Fichier d'enregistrement de la clé de chiffrement AES-GCM
    :return: (dict) La configuration chargée
    """
    # S'assurer que le répertoire existe
    os.makedirs(os.path.dirname(config_file), exist_ok=True)

    # Générer et sauvegarder la clé si elle n'existe pas
    if not os.path.exists(key_file):
        key = gen_key()
        with open(key_file, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(key_file, 'rb') as key_file:
            key = key_file.read()

    # Créer et sauvegarder la configuration chiffrée si elle n'existe pas
    if not os.path.exists(config_file):
        # Configuration à chiffrer
        config_data = {"exemple": "valeur", "nombre": 123}
        nonce, ciphertext, tag = aes_encrypt(config_data, key)
        with open(config_file, 'wb') as config_file:
            config_file.write(nonce + ciphertext + tag)

    # Charger et déchiffrer la configuration
    with open(config_file, 'rb') as config_file:
        nonce = config_file.read(12)
        # Lire tout le reste du fichier
        encrypted_data = config_file.read()
        # Supposer que le tag est les 16 derniers octets de encrypted_data
        ciphertext = encrypted_data[:-16]
        tag = encrypted_data[-16:]
        config = aes_decrypt([nonce, ciphertext, tag], key)

    return config
def save_config(config_data,config_file='config/config.cfg', key_file='config/key.bin'):
    """
    Fonction permettant de sauvegarder la configuration au format JSON avec cryptage AES-GCM
    :param config_file: (str) Fichier d'enregistrement de la configuration
    :param key_file: (str) Fichier d'enregistrement de la clé de chiffrement AES-GCM
    :return: néant
    """
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    if not os.path.exists(key_file):
        key = gen_key()
        with open(key_file, 'wb') as kf:
            kf.write(key)
    else:
        with open(key_file, 'rb') as kf:
            key = kf.read()

    # Sérialiser la configuration en JSON, puis en bytes
    config_json = json.dumps(config_data).encode('utf-8')

    # Chiffrer la configuration
    nonce, ciphertext, _ = aes_encrypt(config_json, key)

    # Écrire les données chiffrées dans le fichier de configuration
    with open(config_file, 'wb') as cf:
        cf.write(nonce + ciphertext)  # Le tag est inclus dans le ciphertext par AESGCM


def get_config(setting,config_file='config/config.cfg', key_file='config/key.bin'):
    """
    Renvoie la valeur de la clé de configuration chargée en mémoire (voir fonction load_config ou
    configuration en construction)
    :param setting: (str) clé de configuration à retourner
    :return: valeur associée à la clé demandée
    """
    config = load_config (config_file, key_file)
    return config.get(setting)

def set_config(setting, value):
    """
    Initialise la valeur de la clé de configuration chargée en mémoire (voir fonction load_config ou
    configuration en construction)
    :param setting: (str) clé de configuration à retourner
    :param value: Valeur à enregistrer
    :return: Néant
    """

def print_config():
    """
    Affiche la configuration en mémoire
    :return: Néant
    """

def reset_config():
    """
    Efface la configuration courante en mémoire
    :return: Néant
    """

def remove_config(setting):
    """
    Retire un paire de clé (setting) / valeur de la configuration courante en mémoire
    :param setting: la clé à retirer du la config courante
    :return: Néant
    """

def validate(msg):
    """
    Devamnde de confirmation par O ou N
    :param msg: (str) Message à afficher pour la demande de validation
    :return: (boolean) Validé ou pas
    """
"""

if __name__ == '__main__':
    config = load_config()
    print("Configuration chargée avec succès :")
    print(config)
    
"""

if __name__== '__main__':
    config_data = {"exemple": "valeur", "nombre": 123}

    # Appel de la fonction save_config
    save_config(config_data,'config/config.cfg','config/key.bin')
    print("la configuration est sauvegarder avec succès")
    








