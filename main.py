"""
Sistema Bancário - Versão 1.0
Desenvolvido para projeto de modernização bancária.
Operações: Depósito, Saque e Extrato
"""

LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

saldo = 0
extrato = ""
numero_saques = 0

menu = """
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_VALOR_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! Limite máximo por saque é R$ 500,00.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n========= EXTRATO =========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("============================\n")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema!")
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")
