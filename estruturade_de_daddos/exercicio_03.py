capacidade_atual, aumento_percentual = map(int, input().split())

#Calcule a nova capacidade do disco de Mithril
nova_capacidade = capacidade_atual + (capacidade_atual * (aumento_percentual / 100) )
novo_valor_inteiro = int(nova_capacidade)
#Imprima a nova capacidade
print(novo_valor_inteiro) 