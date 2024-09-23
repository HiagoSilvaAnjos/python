# Caixa Eletrônico v1.0
saldo = 1000.0  

print("Bem-vindo ao Caixa Eletrônico v1.0")

while True:
    print("\nMenu:")
    print("1. Consultar Saldo")
    print("2. Sacar Dinheiro")
    print("3. Depositar Dinheiro")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo é: R$ {saldo:.2f}")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor a sacar: R$ "))
        saldo -= valor_saque  

    elif opcao == "3":
        valor_deposito = float(input("Informe o valor a depositar: R$ "))
        saldo += valor_deposito  

    elif opcao == "4":
        print("Saindo do Caixa Eletrônico. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
