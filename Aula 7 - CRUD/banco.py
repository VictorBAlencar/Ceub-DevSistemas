#banco.py é para criar e manipular o banco

import sqlite3

conexao = sqlite3.connect("Inventario.db")
cursor = conexao.cursor()

# Função para criar tabela
def iniciar_banco():
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS itens(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT UNIQUE NOT NULL,
      tipo TEXT NOT NULL,
      valor REAL
      )
  """)

# CREATE - Inserir item
def inserir_item(nome,tipo,valor):
    try:
        cursor.execute("INSERT INTO itens (nome,tipo,valor) VALUES(?,?,?)", 
                       (nome,tipo,valor))
        conexao.commit() #commit() salva as alterações
        print("Item inserido com sucesso")
    except sqlite3.IntegrityError: #try catch
        print("Erro: Item já existente")

# READ - Listar ou ler itens 
def listar_itens():
    cursor.execute("SELECT * FROM itens")
    itens = cursor.fetchall() #fetchall() retorna uma lista
    for i in itens: #itens é lista
        print(i) #i é o valor da linha. não precisa de i++

#UDPATE - Atualizar instancia(linha) do item
def atualizar_item(id_item,novo_nome,novo_tipo, novo_valor):
    cursor.execute("UPDATE itens SET nome =?, tipo=?,valor=? WHERE id=?", #id SÓ é usado para identificar o item a ser atualizado
     (novo_nome,novo_tipo, novo_valor, id_item))
    
    if cursor.rowcount > 0: #Se a linha for atualizada
        print("Item atualizado com sucesso!")
        conexao.commit()
    else:
        print("Item não encontrado!")

#DELETE - Excluir item
def excluir_item(id_item):
    cursor.execute("DELETE FROM itens WHERE id = ?",(id_item,))

    if cursor.rowcount > 0: #Se a linha for excluida
        print("Item excluido com sucesso!")
        conexao.commit()
    else:
        print("Item não encontrado!")

#Função para fechar banco
def fechar_banco():
    conexao.commit()
    conexao.close()