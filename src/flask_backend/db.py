import psycopg2
from psycopg2 import sql


from dotenv import load_dotenv
import os

load_dotenv()

# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_PORT = os.getenv("DB_PORT", "5432")


# 配置数据库连接（生产环境建议用环境变量）
DB_NAME = "test_db"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def create_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS data_store (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL
            );
        """)
        conn.commit()

def insert_data(conn, content):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO data_store (content) VALUES (%s)",
            (content,)
        )
        conn.commit()

def query_data(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM data_store")
        return [{"id": row[0], "content": row[1]} for row in cur.fetchall()]
