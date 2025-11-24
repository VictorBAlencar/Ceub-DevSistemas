import json

dados_universidade = { #chaves em minúsculo
    "universidade" : "CEUB",
    "ano_letivo" : 2025,
    "aprovados" : True,
    "alunos" : [
        {"nome" : "Ana Silva", "nota" : 9.4, "presenca" : "100%"}, #dicionário dentro de uma lista
        {"nome" : "Tom Kevin", "nota" : 8.0, "presenca" : "86%"},
        {"nome" : "Ted Nill", "nota" : 10.0, "presenca" : "90%"}
    ]
}

#Escrita de JSON

try:
    with open("Aula 11.2 - JSON/dados_universidade.json", "w", encoding = "utf-8") as f:
        json.dump(dados_universidade, f, indent = 4, ensure_ascii = False)
    print("Arquivo criado com sucesso!")
except Exception as e:
    print("Erro: ", e)

########################################################################################

#Leitura de JSON

try:
    with open("Aula 11.2 - JSON/dados_universidade.json", "r", encoding = "utf-8") as f:
        dados = json.load(f)
        print(f"Universidade: {dados["universidade"]}")
        print("\n Lista de Alunos: ")
        for aluno in dados["alunos"]:
            print(f" - {aluno["nome"]}, Nota: {aluno["nota"]}, Presença: {aluno["presenca"]}")
except FileNotFoundError:
    print("Arquivo não encontrado!")
except json.JSONDecodeError:
    print("O arquivo existe, mas o json não é válido!")