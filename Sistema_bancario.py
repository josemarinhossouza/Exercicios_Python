menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

quantidade_saque = 0
saldo = 0
extrato = []

while True:
    
    iniciar = input(menu)

    # Substituímos o encadeamento de IFs pelo MATCH
    match iniciar:
        
        case 'd':
            deposito = float(input("Digite o valor do depósito: "))

            if deposito >= 0:
                saldo += deposito
                # Adicionado o :.2f para salvar no extrato com duas casas decimais
                extrato.append(f"> Valor depositado: R$ {deposito:.2f}")

        case 's':
            if quantidade_saque < 3 and saldo > 0:
                # Adicionado o :.2f no saldo atual exibido na pergunta
                sacar = float(input(f"Seu saldo atual é R$ {saldo:.2f} Digite o valor do saque: "))

                if sacar <= 500:
                    quantidade_saque += 1
                    saldo -= sacar
                    # Adicionado o :.2f para salvar no extrato com duas casas decimais
                    extrato.append(f"> Valor sacado R$: {sacar:.2f}")
                else:
                    # CORRIGIDO: Agora o print funciona corretamente!
                    print("O valor máximo de saque é R$ 500,00")

            elif saldo == 0: 
                # Adicionado o :.2f no saldo exibido no aviso
                print(f"Seu saldo atual é R$ {saldo:.2f}. Faça depósito para realizar a operação de saque")

            elif quantidade_saque == 3:
                print("Você atingiu o limite de saque diário")

            elif sacar > saldo:
                # Adicionado o :.2f no saldo exibido no aviso
                print(f"Você não tem saldo suficiente. Seu saldo atual é R$ {saldo:.2f}")

        case 'e':
            # Corrigidos os erros de digitação ("atual" e "extrato") e adicionado o :.2f
            print(f"Seu saldo atual é: R$ {saldo:.2f} \nSeu extrato:")
            
            for movimentacao in extrato:
                print(movimentacao)

        case 'q':
            print("Operação finalizada!")
            break

        case _:
            print("Opção inválida! Por favor, selecione uma opção do menu.")
