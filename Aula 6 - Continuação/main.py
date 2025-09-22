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

#def é função
def inserir_pedidos(c, v, s): #cliente_id, valor, status --> simplificar
    cursor.execute("INSERT INTO pedidos(cliente_id, valor, status) VALUES(?, ?, ?)", (c, v, s)) #? ? ? são placeholders 

#ctrl k + ctrl c --> comentar linhas
#ctrl k + ctrl u --> descomentar linhas

#inserir manualmente --> precisa de placeholders e da função def antes
# inserir_pedidos(22, 400.00, 'concluido')
# inserir_pedidos(22, 150.50, 'pendente')
# inserir_pedidos(14, 39.50, 'cancelado')
# inserir_pedidos(42, 1000.00, 'pendente')

#Atualizar campo pelo id
cursor.execute("UPDATE pedidos SET status = 'concluido' WHERE id = 3")

#Atualizar multiplos campos ao mesmo tempo
cursor.execute("UPDATE pedidos SET valor = 33.33, status = 'pendente' WHERE id = 2")

#Atualizar multiplas linhas
cursor.execute("UPDATE pedidos SET status = 'cancelado' WHERE status = 'pendente'")

#Atualizar um campo por outro valor(cliente_id)
cursor.execute("UPDATE pedidos SET status = 'pendente' WHERE cliente_id = 42")

#Atualizar com condição
cursor.execute("UPDATE pedidos SET status = 'cancelado' WHERE valor > 100")

conexao.commit() #salva e envia as alterações
conexao.close() #garantir que o banco seja fechado