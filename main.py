from estoque import *

def menu():
    while True:
        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Listar produtos (ordem alfabética)")
        print("4. Comprar produto")
        print("0. Sair")

        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            nome = input("Nome do produto: ").strip()
            quantidade = int(input("Quantidade: "))
            valor = float(input("Valor: "))
            adicionar_produto(nome, quantidade, valor)

        elif opc == "2":
            listar_produtos()

        elif opc == "3":
            listar_produtos_ordenados()

        elif opc == "4":
            nome = input("Nome do produto: ").strip()
            qtd = int(input("Quantidade desejada: "))
            comprar_produto(nome, qtd)

        elif opc == "0":
            print("👋 Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
