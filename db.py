from psycopg2 import connect
from psycopg2 import extensions
from psycopg2 import sql


user: str = "username"
password: str = "password"
host: str = "127.0.0.1"
port: str = "5432"


def execute(query: str, database: str = "default"):
    """
        Used to make SQL-requests to SQLite database within a single transaction.
        
        query: str - provided SQL-query.
        database: str -
            database name is used:
                to ensure provided query is about to be made for needed database;
                to make 'DROP DATABASE' & 'CREATE DATABASE' queries;
            'default' database is used to make 'DROP DATABASE' & 'CREATE DATABASE' queries for working database.
    """
    
    with connect(user=user, password=password, host=host, port=port, database=database) as connection:
        with connection.cursor() as cursor:
            connection.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            
            sqlified_query = sql.SQL(query)
            identifier = sql.Identifier(database)
            execution_command = sqlified_query.format(identifier)
            
            cursor.execute(execution_command)
            
            if "SELECT" in query: return cursor.fetchall()
