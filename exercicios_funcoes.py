def imprimir(n):
    for i in range(1, n + 1):

        linha = "   ".join([str(i)] * i)
        print(linha)

n = int(input("Digite um número inteiro:  "))
imprimir(n)        