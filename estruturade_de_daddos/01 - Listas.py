# Solicitando a entrada do usuário
quantidade_passos = int(input())

# Verificando se a quantidade de passos é positiva
if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
else:
    # Iterando sobre a quantidade de passos
    for passo in range(1, quantidade_passos + 1):
        if passo == 1:
            print(f"Explorador: {passo} passo")
        else:
            print(f"Explorador: {passo} passos")