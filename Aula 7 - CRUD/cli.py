#serviria como main --> cli
#utilizaria as funções do banco

import sys
import sqlite3
import banco as inventario


def mostrar_menu():
    print("---Inventario---")
    print("1 - Inserir Item")
    print("2 - Listar Itens")
    print("3 - Atualizar Item")
    print("4 - Excluir Item")
    print("5 - Sair")

def insert(): #python é top down --> funções abaixo só podem ser chamadas depois de serem declaradas
    nome = input("Digite o nome do item: ").strip() #strip é trim --> remover espaços
    tipo = input("Digite o tipo do item: ").strip()
    try:
        valor = float(input("Digite o valor do item: ")) #input é string, é convertido para float
    except ValueError:
        print("Erro: Digite um valor float")
    
    inventario.inserir_item(nome,tipo,valor)


def main():
    inventario.iniciar_banco
    while(True): #loop infinito --> atenção à fim do loop
        mostrar_menu()
        opcao = input("Digite uma opção: ") #input() retorna uma string para servir como opção
        match opcao: #match case é switch case
            case "1":
                insert()
            case "2":
                print("Listar Itens") #Placeholder
            case "3":
                print("Atualizar Item") #Placeholder
            case "4":
                print("Excluir Item") #Placeholder
            case "5":
                print("Sair") #Placeholder
                inventario.fechar_banco() #Placeholder
                sys.exit(0) #Placeholder

main() #função principal para fazer rodar