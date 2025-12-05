import mariadb
import os
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
def get_db_connection():
    conn = mariadb.connect(
        user=USER,
        password=PASSWORD,
        host="10.200.11.21",
        port=3306,
        database="smartdb"
    )

    return conn




