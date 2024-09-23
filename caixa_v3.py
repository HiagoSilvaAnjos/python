# Caixa Eletrônico v3.0
saldo = 1000.0  
extrato = ""  
senha = "1234"  
historico_mensagens = []  # Lista de mensagens para o gerente
maior_saldo = saldo  # Para verificar se o cliente teve mais de R$ 10.000,00

print("Bem-vindo ao Caixa Eletrônico v3.0")

senha_informada = input("Digite sua senha para acessar o caixa eletrônico: ")

if senha_informada != senha:
    print("Senha incorreta. Acesso negado.")
else:
    while True:
        print("\nMenu:")
        print("1. Consultar Saldo")
        print("2. Sacar Dinheiro")
        print("3. Depositar Dinheiro")
        print("4. Transferência")
        print("5. Pagar Contas")
        print("6. Recarga de Celular")
        print("7. Extrato")
        print("8. Solicitar Empréstimo")
        print("9. Cancelar Conta")
        print("10. Pix")
        print("11. Falar com o Gerente")
        print("12. Ler Histórico de Mensagens")
        print("13. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao.isnumeric():
            opcao = int(opcao)
        else:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == 1:
            print(f"Seu saldo é: R$ {saldo:.2f}")

        elif opcao == 2:
            valor_saque = float(input("Informe o valor a sacar: R$ "))
            senha_informada = input("Digite sua senha para confirmar: ")
            if senha_informada == senha:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                else:
                    print("Saldo insuficiente para realizar o saque.")
            else:
                print("Senha incorreta. Saque não autorizado.")

        elif opcao == 3:
            valor_deposito = float(input("Informe o valor a depositar: R$ "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            else:
                print("Valor inválido para depósito. Deve ser um valor positivo.")

        elif opcao == 4:
            valor_transferencia = float(input("Informe o valor a transferir: R$ "))
            senha_informada = input("Digite sua senha para confirmar: ")
            if senha_informada == senha:
                if valor_transferencia <= saldo:
                    saldo -= valor_transferencia
                    extrato += f"Transferência: R$ {valor_transferencia:.2f}\n"
                else:
                    print("Saldo insuficiente para realizar a transferência.")
            else:
                print("Senha incorreta. Transferência não autorizada.")

        elif opcao == 5:
            print("Opções de pagamento de contas:")
            print("1. Internet")
            print("2. Energia")
            print("3. Água")
            opcao_conta = input("Escolha uma opção: ")
            valor_conta = float(input("Informe o valor da conta a ser paga: R$ "))
            senha_informada = input("Digite sua senha para confirmar: ")
            if senha_informada == senha:
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
            else:
                print("Senha incorreta. Pagamento não autorizado.")

        elif opcao == 6:
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
            
            senha_informada = input("Digite sua senha para confirmar: ")
            if senha_informada == senha:
                if valor_recarga <= saldo:
                    saldo -= valor_recarga
                    extrato += f"Recarga de celular: R$ {valor_recarga:.2f}\n"
                else:
                    print("Saldo insuficiente para realizar a recarga.")
            else:
                print("Senha incorreta. Recarga não autorizada.")

        elif opcao == 7:
            print("\nExtrato de Transações:")
            print(extrato if extrato else "Nenhuma transação realizada.")

        elif opcao == 8:
            valor_emprestimo = float(input("Informe o valor do empréstimo: R$ "))
            saldo += valor_emprestimo
            extrato += f"Empréstimo: R$ {valor_emprestimo:.2f}\n"

        elif opcao == 9:
            motivo_cancelamento = input("Informe o motivo do cancelamento da conta: ")
            print("Saldo restante:")
            print("1. Sacar")
            print("2. Transferir para outra conta")
            opcao_cancelamento = input("Escolha uma opção: ")
            if opcao_cancelamento == "1":
                valor_saque = float(input("Informe o valor a sacar: R$ "))
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    extrato += f"Saque na cancelamento: R$ {valor_saque:.2f}\n"
                else:
                    print("Saldo insuficiente para realizar o saque.")
            elif opcao_cancelamento == "2":
                valor_transferencia = float(input("Informe o valor a transferir: R$ "))
                if valor_transferencia <= saldo:
                    saldo -= valor_transferencia
                    extrato += f"Transferência na cancelamento: R$ {valor_transferencia:.2f}\n"
                else:
                    print("Saldo insuficiente para realizar a transferência.")
            print(f"Conta cancelada. Motivo: {motivo_cancelamento}.")
            break

        elif opcao == 10:
            print("Escolha uma chave Pix:")
            print("1. CPF")
            print("2. E-mail")
            print("3. Telefone")
            opcao_pix = input("Escolha uma opção: ")
            chave_pix = input("Digite a chave Pix: ")
            valor_pix = float(input("Informe o valor a transferir: R$ "))
            senha_informada = input("Digite sua senha para confirmar: ")
            if senha_informada == senha:
                if valor_pix <= saldo:
                    saldo -= valor_pix
                    extrato += f"Pix: R$ {valor_pix:.2f} para {chave_pix}\n"
                else:
                    print("Saldo insuficiente para realizar o Pix.")
            else:
                print("Senha incorreta. Pix não autorizado.")

        elif opcao == 11:
            mensagem = input("Digite sua mensagem para o gerente: ")
            historico_mensagens.append(mensagem)
            print("Mensagem enviada ao gerente.")

        elif opcao == 12:
            print("\nHistórico de Mensagens:")
            print("\n".join(historico_mensagens) if historico_mensagens else "Nenhuma mensagem enviada.")

        elif opcao == 13:
            print("Saindo do Caixa Eletrônico. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

        # Verifica se o saldo foi maior que R$ 10.000,00 em algum momento
        if saldo > 10000:
            maior_saldo = saldo

        # Submenu para clientes que tiveram mais de R$ 10.000,00
        if maior_saldo > 10000:
            print("\nMenu de Serviços Exclusivos:")
            print("1. Poupança")
            print("2. Cartão de Crédito")
            print("3. Financiamento")
            print("4. Consignado")
            print("5. Investimentos")
            print("6. Compras")
            print("7. Cashback")
            print("8. Câmbio")
            print("Todos os serviços estão em manutenção no momento.")
