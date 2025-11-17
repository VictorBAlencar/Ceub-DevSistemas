from flask import Flask, request, jsonify 
#para funcionar em json

app = Flask(__name__)

produtos = [
    {"id": 1,"nome": "Espada","preco": 100},
    {"id": 2,"nome": "Escudo","preco": 200.50},
    {"id": 3,"nome": "Armadura","preco": 300.30}
]

#Rotas
@app.route("/")
def home():
    return "Bem-Vindo à loja de itens!"

@app.route("/produto", methods = ["GET"])
def get_produtos():
    return jsonify(produtos)

@app.route("/produto/<int:id>", methods = ["GET"]) # @ - annotation precisa de uma função 
def get_produto(id):
    for p in produtos: #cada elemento na lista é um "p"
        if p["id"] == id:
            return jsonify(p) #id é a chave key, o valor ao lado é o value
    return jsonify({"erro": "Produto não encontrado."}), 404

@app.route("/produto", methods = ["POST"])
def adicionar_produto():
    novo = request.get_json()
    produtos.append(novo) #adiciona no final != insert(usa valor e id)
    return jsonify(novo), 201 #201 se funcionar

@app.route("/produto/<int:id>", methods = ["PUT"])
def atualizar_produto(id):
    dados_novo = request.get_json()
    for p in produtos:
        if p["id"] == id:
            p.update(dados_novo) #p.update é recurso de listas do python
            return jsonify(p)
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route("/produto/<int:id>", methods = ["DELETE"])
def deletar_produto(id):
    for p in produtos:
        if p["id"] == id:
            produtos.remove(p)
            return jsonify({"mensagem":"produto removido!"}), 204
    return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == "__main__": #no final do código, entra em servidor local de teste
    app.run(debug = True)
