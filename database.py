import mysql.connector
import config


def connect_db():
    connection = mysql.connector.connect(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        database=config.DATABASE,
    )
    return connection
