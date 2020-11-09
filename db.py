from psycopg2 import connect
from psycopg2 import extensions
from psycopg2 import sql


user: str = "airatk"
password: str = "12LLabteksaB21"
host: str = "127.0.0.1"
port: str = "5432"


def execute(query: str, database: str = "airatk"):
    with connect(user=user, password=password, host=host, port=port, database=database) as connection:
        with connection.cursor() as cursor:
            connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            
            cursor.execute(sql.SQL(query).format(sql.Identifier(database)))
            
            if "SELECT" in query: return cursor.fetchall()
