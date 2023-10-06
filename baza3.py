# relacyjna baza danych sql
# sqlite baza w jednym pliku

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    insert_sql = "INSERT INTO software (id, name, price) VALUES (1, 'Python', 1000);"
    cursor = sql_connection.cursor()
    print("Baza danych zostala podłaczona")
    cursor.execute(insert_sql)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze niezaleznie czy był bład czy nie
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostala zamknieta")  # polaczenie z DB zostalo zamkniete
