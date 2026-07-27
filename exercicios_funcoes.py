def imprimir(n):
    for i in range(1, n + 1):

        linha = "   ".join([str(i)] * i)
        print(linha)

n = int(input("Digite um número inteiro:  "))
imprimir(n)        

# Como funciona:
# O for i in range(1, n + 1) percorre de 1 até n.

# [str(i)] * i cria uma lista com o número convertido em string repetido i vezes.

# " ".join(...) junta os elementos da lista com três espaços entre eles (como no seu exemplo).

# print(linha) exibe cada linha no terminal.