import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('db.sqlite3')

# Criar um cursor
cursor = conn.cursor()

# Executar uma consulta
cursor.execute("DELETE FROM arduino_heartratedata")
conn.commit()


# Fechar o cursor e a conexão
cursor.close()
conn.close()


