import json
import os

ARQUIVO_PRODUTOS = "produtos.json"


def carregar_produtos():
    
    if os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_produtos(produtos):
   
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)


def gerar_novo_id(produtos):
   
    if not produtos:
        return 1
    return max(p["id"] for p in produtos) + 1


def adicionar_produto(nome, quantidade, valor):
    
    produtos = carregar_produtos()
    novo_produto = {
        "id": gerar_novo_id(produtos),
        "produto": nome,
        "quantidade": quantidade,
        "valor": valor
    }
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    print(f"✅ Produto '{nome}' adicionado com sucesso!")


def listar_produtos():
   
    produtos = carregar_produtos()
    if not produtos:
        print("❌ Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(f"ID: {p['id']} | {p['produto']} - {p['quantidade']} unid. - R$ {p['valor']:.2f}")


def listar_produtos_ordenados():
    
    produtos = carregar_produtos()
    produtos.sort(key=lambda p: p["produto"].lower())
    for p in produtos:
        print(f"ID: {p['id']} | {p['produto']} - {p['quantidade']} unid. - R$ {p['valor']:.2f}")


def comprar_produto(nome, qtd_comprar):
    
    produtos = carregar_produtos()
    for p in produtos:
        if p["produto"].lower() == nome.lower():
            if p["quantidade"] >= qtd_comprar:
                total = p["valor"] * qtd_comprar
                print(f"💰 Total da compra: R$ {total:.2f}")
                confirmar = input("Deseja confirmar a compra? (s/n): ").strip().lower()
                if confirmar == "s":
                    p["quantidade"] -= qtd_comprar
                    salvar_produtos(produtos)
                    print(f"✅ Compra realizada! Restam {p['quantidade']} unidades de {p['produto']}.")
                else:
                    print("❌ Compra cancelada.")
            else:
                print("⚠️ Quantidade indisponível em estoque.")
            return
    print("❌ Produto não encontrado.")
