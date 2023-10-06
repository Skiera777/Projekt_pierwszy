# relacyjna baza danych sql
# sqlite baza w jednym pliku

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = '''
    CREATE TABLE developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEX NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''
    #real = odpowiednik float
    with open('tables.sql', 'r') as file:
        sql_script = file.read()
    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")

    #cursor.execute(query) # wykonanie query w bazie
    #sql_connection.commit() # trwałe zapamnietanie zmian w bazie
    cursor.executescript(sql_script) #wykonanie kodu z wczytanego skryptu

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze niezaleznie czy był bład czy nie
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostala zamknieta")  # polaczenie z DB zostalo zamkniete
