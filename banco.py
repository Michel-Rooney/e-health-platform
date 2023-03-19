# import sqlite3

# # Conectar ao banco de dados
# conn = sqlite3.connect('db.sqlite3')

# # Criar um cursor
# cursor = conn.cursor()

# # Executar uma consulta
# cursor.execute("DELETE FROM platform_health_note")
# conn.commit()


# # Fechar o cursor e a conexão
# cursor.close()
# conn.close()


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(lista[:10:-1])