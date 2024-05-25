import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

# Database configuration
DB_HOST = 'postgres'
DB_NAME = 'db'
DB_USER = 'admin'
DB_PASSWORD = 'admin'

# Create a PostgreSQL connection pool
db_pool = pool.SimpleConnectionPool(
    minconn=1,  # Minimum number of connections in the pool
    maxconn=10,  # Maximum number of connections in the pool
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Define a function to get a database connection from the pool
def get_db_conn():
    connection = db_pool.getconn()
    db_conn = connection.cursor(cursor_factory=RealDictCursor)  # Use RealDictCursor for dictionary-like results
    try:
        yield db_conn
    finally:
        db_conn.close()
        db_pool.putconn(connection)