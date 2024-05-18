numeros = set([1,2,3,1,3,4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))

# nao podemos acessar o valor com o indice do set, temos que converter-lo em uma lista
carrosl = list(carros)

print (carrosl)

conjunto_a = {1,2}
conjunto_b = {3,4}
conjunto_a.union(conjunto_b)

#uniao
# intercessao
conjunto_a.intersection(conjunto_b)
#diferenca = difference

conjunto_a.difference(conjunto_b)


#symmetric_difference 

conjunto_a.symmetric_difference(conjunto_b)

#issubset esta contido em A que nao esta contido em B

conjunto_a.issubset(conjunto_b) #True
conjunto_b.issubset(conjunto_a) #false


#isdisjoint as partes que nao se tocam

conjunto_a.isdisjoint(conjunto_b)

#add
sorteio = {1,2,3}
sorteio.add(4)
print(sorteio)