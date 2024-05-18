# Lista para armazenar os itens
itens = []
entrada = input("Informe uma2 informação ou 'fim' para encerrar: ")
#TODO: Solicite os itens ao usuário
itens.append(entrada)

# Solicitando ao usuário para inserir as informações
print("Por favor, insira até três informações.")

while len(itens) < 3:
    entrada = input("Informe uma informação: ")
    itens.append(entrada)
    
    if len(itens) == 3:
        print("Você atingiu o limite de 3 informações.")
        break

# Imprimindo as informações inseridas pelo usuário
print("As informações inseridas foram:")
for info in itens:
    print(info)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")