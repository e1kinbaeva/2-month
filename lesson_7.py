"СУБД - Система управления базой данных"
"БД - База Данных"
"SQlite3"


"Работа с функцией"
import sqlite3

connection = sqlite3.connect("backend.db")
cursor  = connection.cursor()

"Sozdanie tabl"

cursor.execute(""" CREATE TABLE students(
             id 
)""")

