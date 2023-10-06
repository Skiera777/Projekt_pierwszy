# relacyjna baza danych sql
# sqlite baza w jednym pliku

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")
except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych")
finally:  # wykonuje sie zawsze niezaleznie czy był bład czy nie
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostala zamknieta")  # polaczenie z DB zostalo zamkniete
