import sqlite3
import getpass

# conn = sqlite3.connect('miaplicacion.db')
# cursor = conn.cursor()

# data = [
    #     (1, "luismi", "patito007"),
    #     (2, "nacho", "naranja3"),
    #     (3, "otromas", "alaporra")
    # ]

# cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)")
# cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", data) # para muchos datos
# cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (4, "lagarto", "show45"))
# conn.commit() # siempre después de INSERT para salvar los datos

# rows = cursor.execute('SELECT * FROM users')

# for row in rows:
#     print(row)

# cursor.close()
# conn.close()

def main():
    username = str(input("Nombre de usuario: "))
    password = str(getpass.getpass("Ingresa contraseña: "))

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    cursor = conn.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)")
    #res = cursor.execute('SELECT name FROM sqlite_master') # paa saber el nombre de las tablas existentes
    #print("Las tablas existentes son: ", list(res))

    # data = [
    #     (1, "luismi", "patito007"),
    #     (2, "nacho", "naranja3"),
    #     (3, "otromas", "alaporra")
    # ]
    # cursor.executemany("INSERT INTO users VALUES(?, ?, ?)", data)
    # conn.commit() # Remember to commit the transaction after executing INSERT
    
    query = str(f"SELECT id FROM users WHERE username='{username}' AND password='{password}'")
    rows = cursor.execute(query)
    data = rows.fetchone()
    print("imprimiendo data: ", list(data))
    cursor.close()
    conn.close()
    return data

if __name__=='__main__':
    main()