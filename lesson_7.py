"СУБД - Система управления базой данных"
"БД - База Данных"
"SQlite3"


"Работа с функцией"
import sqlite3

connection = sqlite3.connect("backend.db")
cursor  = connection.cursor()

"Sozdanie tabl"

cursor.execute(""" CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR (30) NOT NULL,
               attendance DOUBLE (3 , 2) DEFAULT 0.0,
               hobby TEXT DEFAULT NULL,
               is_payment BOOLEAN DEFAULT FALSE,
               birthday DATE

               
)""")

"int = INT, INTEGER, BIGINT"
"str = TEXT, VARCHAR"
"float = FLOAT, REAL, DOUBLE"
"bool = BOOLEAN "

