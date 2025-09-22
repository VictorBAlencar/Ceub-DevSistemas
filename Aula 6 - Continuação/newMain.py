import sqlite3

conexao = sqlite3.connect('loja.db') #cria o banco
cursor = conexao.cursor() #executar comandos

# """ para quebra de linha

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS pedidos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INT NOT NULL,
    valor REAL CHECK(valor > 0),
    status TEXT CHECK(status IN('pendente', 'concluido', 'cancelado'))
    )           
""")

#query --> não precisa de placeholders
''' -> comentário em bloco
'''
cursor.execute("""
    INSERT INTO pedidos(cliente_id, valor, status) VALUES
        (45, 45.33, 'concluido'),      
        (45, 78.96, 'pendente'),
        (23, 45.33, 'pendente'),
        (23, 78.96, 'cancelado'),
        (14, 45.33, 'concluido'),
        (87, 12.33, 'cancelado')      
""")


#Deletar pelo id
#cursor.execute("DELETE FROM pedidos WHERE id = 3")

#Deletar por critério/condição
#cursor.execute("DELETE FROM pedidos WHERE status = 'concluido'")

#Deletar por critério numérico
#cursor.execute("DELETE FROM pedidos WHERE valor < 50")

#Deletar tudo --> salva os autoincrements(sqlite_sequence -> confere o nome e sequencia da tabela)
#cursor.execute("DELETE FROM pedidos")

#Resetar autoincrements
#cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'pedidos'")

conexao.commit() #salva e envia as alterações

#Resetar ids
#cursor.execute("VACUUM;") #apaga o lixo

conexao.close() #garantir que o banco seja fechado