# Caixa Eletrônico v2.0
saldo = 1000.0  
extrato = "" 

print("Bem-vindo ao Caixa Eletrônico v2.0")

while True:
    print("\nMenu:")
    print("1. Consultar Saldo")
    print("2. Sacar Dinheiro")
    print("3. Depositar Dinheiro")
    print("4. Transferência")
    print("5. Pagar Contas")
    print("6. Recarga de Celular")
    print("7. Extrato")
    print("8. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo é: R$ {saldo:.2f}")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor a sacar: R$ "))
        if valor_saque <= saldo:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
        else:
            print("Saldo insuficiente para realizar o saque.")

    elif opcao == "3":
        valor_deposito = float(input("Informe o valor a depositar: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Valor inválido para depósito. Deve ser um valor positivo.")

    elif opcao == "4":
        valor_transferencia = float(input("Informe o valor a transferir: R$ "))
        if valor_transferencia <= saldo:
            saldo -= valor_transferencia
            extrato += f"Transferência: R$ {valor_transferencia:.2f}\n"
        else:
            print("Saldo insuficiente para realizar a transferência.")

    elif opcao == "5":
        print("Opções de pagamento de contas:")
        print("1. Internet")
        print("2. Energia")
        print("3. Água")
        
        opcao_conta = input("Escolha uma opção: ")
        valor_conta = float(input("Informe o valor da conta a ser paga: R$ "))
        
        if valor_conta <= saldo:
            saldo -= valor_conta
            extrato += f"Pagamento de conta: R$ {valor_conta:.2f} - "
            if opcao_conta == "1":
                extrato += "Internet\n"
            elif opcao_conta == "2":
                extrato += "Energia\n"
            elif opcao_conta == "3":
                extrato += "Água\n"
            else:
                print("Opção de conta inválida.")
        else:
            print("Saldo insuficiente para pagar a conta.")

    elif opcao == "6":
        print("Opções de recarga de celular:")
        print("1. R$ 10,00")
        print("2. R$ 20,00")
        print("3. R$ 50,00")
        
        opcao_recarga = input("Escolha uma opção: ")
        if opcao_recarga == "1":
            valor_recarga = 10.0
        elif opcao_recarga == "2":
            valor_recarga = 20.0
        elif opcao_recarga == "3":
            valor_recarga = 50.0
        else:
            print("Opção de recarga inválida.")
            continue
        
        if valor_recarga <= saldo:
            saldo -= valor_recarga
            extrato += f"Recarga de celular: R$ {valor_recarga:.2f}\n"
        else:
            print("Saldo insuficiente para realizar a recarga.")

    elif opcao == "7":
        print("\nExtrato de Transações:")
        print(extrato if extrato else "Nenhuma transação realizada.")

    elif opcao == "8":
        print("Saindo do Caixa Eletrônico. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
