def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "aspera" and cor == "vermelha":
        return "A fruta é um morango!"
    elif peso >= 130 and textura == "suave" and cor == "vermelha":
        return "A fruta é uma maçã!"
    elif peso >= 120 and textura == "suave" and cor == "laranja":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "aspera" and cor == "amarela":
        return "A fruta é uma banana!"
    else:
        return "Não foi possível classificar a fruta."

# Entrada do usuário
peso_fruta = float(input("Peso da fruta (em gramas): "))
textura_fruta = input("Textura da fruta (suave ou aspera): ")
cor_fruta = input("Cor da fruta (vermelha, laranja ou amarela): ")

# Chamada da função de previsão e saída da previsão
print(prever_fruta(peso_fruta, textura_fruta, cor_fruta))