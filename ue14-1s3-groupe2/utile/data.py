import sqlite3

# Constantes
DB_FILENAME = 'C:\\Users\\admin\\helmo\\ue14-1s3-groupe2\\serveur_cles\\data\\victims.sqlite'



def connect_db():
    """
    Initialise la connexion vers la base de donnée
    :return: La connexion établie avec la base de donnée
    """
    try:
        conn = sqlite3.connect(DB_FILENAME)
        print("connection etablie avec sucées")
        return conn
    except Exception as e:
        print(f"une erreur est survenue lors de la connection avec la base de données {e}")
        return None

def insert_data(conn, table, items, data):
    """
    Insère des données de type 'items' avec les valeurs 'data' dans la 'table' en utilisant la connexion 'conn' existante
    :param conn: la connexion existante vers la base de donnée
    :param table: la table dans laquelle insérer les données
    :param items: le nom des champs à insérer
    :param data: la valeur des champs à insérer
    :return: Néant
    """
    try:
        # Création d'une requête SQL dynamique pour l'insertion de données
        sql_query = f"INSERT INTO {table} ({', '.join(items)}) VALUES ({', '.join(['?' for _ in items])})"

        # Utilisation d'un curseur pour exécuter la requête SQL avec les valeurs de données fournies
        with conn:
            conn.execute(sql_query, data)
        print("Données insérées avec succès dans la table", table)
    except sqlite3.Error as e:
        print(f"Erreur lors de l'insertion des données dans la table {table} : {e}")


def select_data(conn, select_query):
    """
    Exécute un SELECT dans la base de donnée (conn) et retourne les records correspondants
    :param conn: la connexion déjà établie à la base de donnée
    :param select_query: la requête du select à effectuer
    :return: les records correspondants au résultats du SELECT
    """
    try:
        # Utilisation d'un curseur pour exécuter la requête SELECT
        cursor = conn.execute(select_query)

        # Récupération des enregistrements
        records = cursor.fetchall()


        # Retour des enregistrements
        return records
    except sqlite3.Error as e:
        print(f"Erreur lors de l'exécution de la requête SELECT : {e}")
        return None

def get_list_victims(conn):
    """
    Retourne la liste des victimes présente dans la base de donnée
    :param conn: la connexion déjà établie à la base de donnée
    :return: La liste des victimes
    """
    try:
        # Définition de la requête SQL pour récupérer toutes les victimes
        select_query = f"SELECT * FROM victims"

        # Appel à la fonction select_data pour exécuter la requête SELECT
        records = select_data(conn, select_query)

        # Retour des enregistrements récupérés
        return records
    except Exception as e:
        print(f"Erreur lors de la récupération de la liste des victimes : {e}")
        return None


def get_list_history(conn, id_victim):
    """
    Retourne l'historique correspondant à la victime 'id_victim'
    :param conn: la connexion déjà établie à la base de donnée
    :param id_victim: l'identifiant de la victime
    :return: la liste de son historique
    """
    try:
        # Définition de la requête SQL pour récupérer l'historique de la victime spécifiée
        select_query = f"SELECT * FROM states WHERE id_victim = {id_victim}"

        # Appel à la fonction select_data pour exécuter la requête SELECT
        history = select_data(conn, select_query)

        # Retour de l'historique récupéré
        return history
    except Exception as e:
        print(f"Erreur lors de la récupération de l'historique pour la victime {id_victim} : {e}")
        return None

def get_state_user(conn, id_victim) :
    """
       Retourne l'état correspondant à la victime 'id_victim'
       :param conn: la connexion déjà établie à la base de donnée
       :param id_victim: l'identifiant de la victime
       :return: l'état de la victime
       """
    try:
        select_query = f"SELECT s.*, v.hash FROM states s JOIN victims v ON s.id_victim = v.id_victim WHERE s.id_victim = {id_victim}"
        return select_data(conn, select_query)

    except Exception as e:
        print(f"Erreur lors de la récupération de l'état de la victime {id_victim} : {e}")
        return None