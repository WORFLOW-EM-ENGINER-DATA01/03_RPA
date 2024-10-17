import psycopg2
from psycopg2 import OperationalError
from psycopg2.extras import execute_values
from domain.types import StockPurchaseList


def connect_to_postgres():
    try:
        connection = psycopg2.connect(
            user="rpa",
            password="password",
            host="db",  # Nom de service dans Docker
            port="5432",  # Port PostgreSQL
            database="postgres"
        )
        print("Yes !")

        return connection

    except OperationalError as e:
        print(f"Oups : {e}")


def create_table(conn):
    try:
        cursor = conn.cursor()

        # Créer la table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS investment (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            quantity INTEGER NOT NULL,
            credit DECIMAL(10, 2) NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()  # Valider les changements

        print("Table 'investment' créée avec succès.")

    except Exception as error:
        print("Erreur lors de la création de la table :", error)


def insert(conn, investments: StockPurchaseList) -> None:
    try:
       
        insert_query = """
            INSERT INTO investment (name, price, quantity, credit)
            VALUES (%s, %s, %s, %s)
            """
        with conn.cursor() as cursor:
            for investment in investments:
                cursor.execute(insert_query, investment)

        conn.commit()

        print("Table hydratée avec succès.")

    except Exception as error:
        print("Erreur lors de l'insertion de la table :", error)
