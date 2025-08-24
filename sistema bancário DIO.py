menu = """
===============
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
===============
>>> """

saldo = 0
LIMITE_DE_VALOR = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposito efetuado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = LIMITE_DE_VALOR
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("\n  EXTRATO:")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        
    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")