import json
import os

def carregar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

def criarusuario(usuarios):
    nome = input("Nome de usuário: ")
    if nome in usuarios:
        print("Usuário já existe.")
        return
    senha = input("senha:")
    usuarios[nome] = {"senha": senha, "saldo": 0.0, "transacoes": []}
    salvar_usuarios(usuarios)
    print("usuario criado com sucesso")

def login(usuarios):
    nome = input("usuario: ")
    senha = input("senha: ")
    if nome in usuarios and usuarios[nome]["senha"] == senha:
        print(f"Bem-vindo, {nome}!")
        menu_banco(nome, usuarios)
    else:
        print("usuaario ou senha incorretos")

def depositar(usuario, usuarios):
    valor = float(input("Valor do depósito: "))
    usuarios[usuario]["saldo"] += valor
    usuarios[usuario]["transacoes"].append(f"Depósito: R${valor:.2f}")
    salvar_usuarios(usuarios)
    print("deposito realizado.")

def sacar(usuario, usuarios):
    valor = float(input("Valor do saque: "))
    if valor > usuarios[usuario]["saldo"]:
        print("saldo insuficiente.")
    else:
        usuarios[usuario]["saldo"] -= valor
        usuarios[usuario]["transacoes"].append(f"Saque: R${valor:.2f}")
        salvar_usuarios(usuarios)
        print("saque realizado com sucesso!")

def extrato(usuario, usuarios):
    print(f"extrato de {usuario}:")
    for t in usuarios[usuario]["transacoes"]:
        print(t)
    print(f"saldo atual: R${usuarios[usuario]['saldo']:.2f}")

def menu_banco(usuario, usuarios):
    while True:
        print("1.Depósito")
        print("2.saque")
        print("3.ver extrato")
        print("4.sair")
        opcao = input("opcao: ")
        if opcao == "1":
            depositar(usuario, usuarios)
        elif opcao == "2":
            sacar(usuario, usuarios)
        elif opcao == "3":
            extrato(usuario, usuarios)
        elif opcao == "4":
            break
        else:
            print("opcao invalida.")

def central():
    usuarios = carregar_usuarios()
    while True:
        print("escolha do sistema bancario")
        print("1.criar usuário")
        print("2.login")
        print("3.sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            criarusuario(usuarios)
        elif opcao == "2":
            login(usuarios)
        elif opcao == "3":
            break
        else:
            print("operçao invaloida!")

central()
