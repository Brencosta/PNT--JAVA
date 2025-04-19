import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f)

def adicionar_tarefa():
    descricao = input("Descrição: ")
    prazo = input("Prazo (YYYY-MM-DD): ")
    tarefa = {"descricao": descricao, "prazo": prazo, "concluida": False}
    tarefas = carregar_tarefas()
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("tarefa adicionada.")

def listar_tarefas():
    tarefas = carregar_tarefas()
    for t in tarefas:
        status = "concluída" if t["concluida"] else "Pendente"
        print(f"{t['descricao']} - Prazo: {t['prazo']} - {status}")

def concluir_tarefa():
    descricao = input("descrição da tarefa a concluir: ")
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["descricao"] == descricao:
            t["concluida"] = True
            break
    salvar_tarefas(tarefas)
    print(" tarefa marcada como concluída.")

def menu():
    while True:
        print(" Adicionar tarefa")
        print("2.Listar tarefas")
        print("3.Concluir tarefa")
        print("4.Sair")
        opcao = input("opcaoo: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            break
        else:
            print("Opcao invalidaa.")
menu()