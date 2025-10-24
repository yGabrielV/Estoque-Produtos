from flask import Flask, request, jsonify
from estoque import *

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "API de Estoque em Python no Render"}

@app.route("/produtos", methods=["GET"])
def listar():
    return jsonify(carregar_produtos())

@app.route("/produtos", methods=["POST"])
def adicionar():
    data = request.json
    if not all(k in data for k in ("produto", "quantidade", "valor")):
        return {"erro": "Campos obrigatórios: produto, quantidade, valor"}, 400
    adicionar_produto(data["produto"], data["quantidade"], data["valor"])
    return {"mensagem": "Produto adicionado com sucesso"}

@app.route("/comprar", methods=["POST"])
def comprar():
    data = request.json
    nome = data.get("produto")
    qtd = data.get("quantidade")
    if not nome or not qtd:
        return {"erro": "Campos obrigatórios: produto, quantidade"}, 400
    produtos = carregar_produtos()
    for p in produtos:
        if p["produto"].lower() == nome.lower():
            if p["quantidade"] >= qtd:
                p["quantidade"] -= qtd
                salvar_produtos(produtos)
                return {"mensagem": f"Compra realizada de {qtd}x {p['produto']}"}
            else:
                return {"erro": "Estoque insuficiente"}, 400
    return {"erro": "Produto não encontrado"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
