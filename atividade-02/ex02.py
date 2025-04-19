import json
import os

ARQUIVO = "estoque.json"
def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_estoque(estoque):
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f)

def adicionar():
    nome = input("nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço unitário: "))
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque = carregar_estoque()
    estoque.append(produto)
    salvar_estoque(estoque)
    print("produto adicionado")

def listar():
    estoque = carregar_estoque()
    total = 0
    print("produtos no estoque:")
    for p in estoque:
        subtotal = p["quantidade"] * p["preco"]
        total += subtotal
        print(f"{p['nome']} - Qtd: {p['quantidade']} - Preço: R${p['preco']:.2f} - Total: R${subtotal:.2f}")
    print(f"valalor total do estoque: R${total:.2f}")

def entrada():
    while True:
        print("adicionar produto")
        print("2.listar produtos")
        print("3.sair")
        opcao = input("opcao: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            break
        else:
            print("opcao invalida!")
entrada()
