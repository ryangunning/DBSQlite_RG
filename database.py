import sqlite3

CREATE_BEANS_TABLE = "CREATE TABLE beans(id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"

INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?, ?, ?);"

GET_ALL_BEANS = "SELECT * FROM beans;"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))