import json
import os

ARQUIVO = "contatos.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_contatos(contatos):
    with open(ARQUIVO, "w") as f:
        json.dump(contatos, f)

def adicionar_contato():
    nome = input("seu nome: ")
    telefone = input("seu telefone: ")
    email = input("seu email: ")
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print("contato adicionado.")

def buscar_contato():
    busca = input("nome a ser procurado": ").lower()
    contatos = carregar_contatos()
    encontrados = [c for c in contatos if busca in c["nome"].lower()]
    if encontrados:
        for c in encontrados:
            print(f"{c['nome']} - {c['telefone']} - {c['email']}")
    else:
        print("nada encontrado")

def operacao():
    while True:
        print("adicionar contato")
        print("2.buscar contato")
        print("3.sair")
        opcao = input("opcao: ")
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            buscar_contato()
        elif opcao == "3":
            break
        else:
            print("Opcao invalida!")

operacao()

