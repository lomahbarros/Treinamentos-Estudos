

lista = []
lista.append({"nome": "Aloma", "nascimento": 1993})
lista.append({"nome": "Matheus", "nascimento": 1994})
lista.append({"nome": "Alícia", "nascimento": 2025})
lista.append({"nome": "", "nascimento": "" })


for pessoa in lista:
    print("\n-- DADOS DA FAMÍLIA --")
    for chave in pessoa:
        print(f"{chave} = {pessoa[chave]}")
  
