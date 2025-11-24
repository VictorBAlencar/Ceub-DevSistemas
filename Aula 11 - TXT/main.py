# Escrita de arquivo .txt

linhas_para_escrever = [
    "Hello World! \n",
    "2nd line \n",
    "Teste de acentuação e ç"
]

# "w" = modo write
# "r" = modo read

# Escrita

try:
    with open("Aula 11 - Arquivos/Meu_Arquivo.txt", "w", encoding = "utf-8") as f: #f de file
        f.write("Este é o cabeçalho. \n")
        f.write("------------------- \n")
        f.writelines(linhas_para_escrever) #escreve várias linhas de uma vez
    print("Arquivo: Meu_Arquivo.txt foi escrito com sucesso!") #caso der certo
except Exception as e: # erro em "e" para printar
    print(f"Ocorreu um erro ao escrever o arquivo: {e}") #caso der errado

###################################################################

#Leitura

try:
    with open("Aula 11 - Arquivos/Meu_Arquivo.txt", "r", encoding = "utf-8") as f: #f de file #r de read o arquivo tem q existir
        print("--- Lendo arquivo linhas por linha --- \n")
        for linha in f:  #linha é semelhante ao i e f é cada linha do arquivo
            print(f"{linha.strip()}") # quebra a linha 
except FileNotFoundError:
    print("Arquivo não encontradao.")
except Exception as e: # erro em "e" para printar
    print(f"Ocorreu um erro ao ler o escrive: {e}")