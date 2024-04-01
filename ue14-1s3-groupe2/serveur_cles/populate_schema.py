import string
import random
import time
import utile.data as data

# valeurs de simulation
fake_victims = [
    ['WORKSTATION', 'c:,e:,f:', 'PENDING', 108],
    ['SERVEUR', 'c:,e:', 'PROTECTED', 23],
    ['WORKSTATION', 'c:,f:', 'INITIALIZE', 0],
    ['WORKSTATION', 'c:,f:,y:,z:', 'PROTECTED', 108]
]

fake_histories1 = [
    ['INITIALIZE', 0],
    ['CRYPT', 0],
    ['CRYPT', 89],
    ['PENDING', 108]
]
#travail git
fake_histories2 = [
    ['INITIALIZE', 0],
    ['CRYPT', 0],
    ['PENDING', 20],
    ['PENDING', 23],
    ['DECRYPT', 23],
    ['PROTECTED', 23]
]

fake_histories3 = [
    ['INITIALIZE', 0]
]

fake_histories4 = [
    ['INITIALIZE', 0],
    ['CRYPT', 0],
    ['CRYPT', 89],
    ['PENDING', 108],
    ['DECRYPT', 65],
    ['DECRYPT', 108],
    ['PROTECTED', 108]
]

fake_histories = {
    1: fake_histories1,
    2: fake_histories2,
    3: fake_histories3,
    4: fake_histories4
}


def simulate_key(longueur=0):
    letters = ".éèàçùµ()[]" + string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(longueur))


def simulate_hash(longueur=0):
    letters = string.hexdigits
    return ''.join(random.choice(letters) for i in range(longueur))


def main():
    conn = data.connect_db()
    if conn is None:
        print("Impossible de se connecter à la base de données.")
        return
    for victim_data in fake_victims:
        data.insert_data(conn, 'victims', ['os', 'disks', 'hash', 'key'], victim_data)
    for victim_id, histories in fake_histories.items():
        for state_data in histories:
            state_data.insert(0, victim_id)  # Insérer l'ID de la victime au début de la liste
            data.insert_data(conn, 'states', ['id_victim', 'state', 'datetime'], state_data)
    exit(0)

if __name__ == '__main__':
    main()
