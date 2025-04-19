import json
import os

ARQUIVO = "assentos.json"

def carregar_assentos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    else:
        return {f"{linha}{num}": False for linha in "ABCDE" for num in range(1, 6)}

def salvar_assentos(assentos):
    with open(ARQUIVO, "w") as f:
        json.dump(assentos, f)

def mostrar_mapa(assentos):
    print("mapa de Assentos:")
    for linha in "ABCDE":
        linha_assentos = ""
        for num in range(1, 6):
            chave = f"{linha}{num}"
            status = "[x]" if assentos[chave] else "[ ]"
            linha_assentos += f"{chave} {status}  "
        print(linha_assentos)
    print("[x] Reservado  [ ] Disponível")

def reservar_assento(assentos):
    assento = input("digite o codigo do assento ex: B9: ").upper()
    if assento in assentos:
        if assentos[assento]:
            print("assento esta reservado")
        else:
            assentos[assento] = True
            salvar_assentos(assentos)
            print("Reserva realizada com sucesso")
    else:
        print("assento invalido!")

def cancelar_reserva(assentos):
    assento = input("digite o codigo do assento para cancelar (ex: B3): ").upper()
    if assento in assentos:
        if assentos[assento]:
            assentos[assento] = False
            salvar_assentos(assentos)
            print("reserva cancelada.")
        else:
            print("esse assento não está reservado.")
    else:
        print("assento invalido")

def menu():
    assentos = carregar_assentos()
    while True:
        print("sistema de Reservas ")
        print("1.ver mapa de assentos")
        print("2.reservar assento")
        print("3.cancelar reserva")
        print("4.sair")
        opcao = input("escolha uma opcao: ")

        if opcao == "1":
            mostrar_mapa(assentos)
        elif opcao == "2":
            reservar_assento(assentos)
        elif opcao == "3":
            cancelar_reserva(assentos)
        elif opcao == "4":
            break
        else:
            print("escolha invalida!")
menu()
