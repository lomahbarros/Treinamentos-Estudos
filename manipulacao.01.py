numeros = [1,2,3,55,98,2,78]
print(numeros) #printa lista

print(numeros[3]) #printa o indice escolhido

numeros[0] = 999 # substitue o valor 999 ao valor do indice 0 que era 1

print(numeros)

numeros.append(2026) #insere ao final da lista

print(numeros)

numeros.insert(1,500) #insere nesse indice

print(numeros)

numeros.remove(2026) #remove o valor
print(numeros)

numeros.pop(3) #remove com o indice
print(numeros)