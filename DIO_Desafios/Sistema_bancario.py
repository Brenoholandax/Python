menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


=> """

Saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True :
    opcao = input(menu)
    if opcao == "1" :
        valor = float(input("Informe o valor de deposito"))
        
        if valor > 0:
            Saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação Falhou! o valor informado é invalido")
    elif opcao == "2":
        valor = float(input("informe o valor do saque:"))
        
        excedeu_saldo = valor > Saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("operação falhou! Você não tem saldo suficiente")
            
        elif excedeu_limite : 
            print("operação falhou! O valor dop saque excede o limite.")
        
        elif excedeu_saques :
            print("Operação falhou! numero maximo de saques excedido")
        
        elif valor > 0:
            Saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    
    elif opcao == "3":
        print("\n========EXTRATO========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${Saldo:.2f}")
        print("================================")
    
    elif opcao == "4":
        print("Opcao invalida")            
             