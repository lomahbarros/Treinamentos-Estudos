#Codigos do Professor!


# dados = {"nome": "João", "twitter": "jpjust", "nascimento": 1982}

# for x in dados:
#     print(dados[x])



# dados = {"nome": "João", "twitter": "jpjust", "nascimento": 1982}

# for chave in dados:
#   print(f"{chave} = {dados[chave]}")


dados1 = {"nome": "Aloma", "Sobrenome": "Barros", "Ano": 1993}

for dadosaloma in dados1:
  # print(dados1) - "Dessa forma  o for percorre cada chave do dicionário, e como o print(dados1) imprime o dicionário inteiro, ele aparece repetido tantas vezes quanto o número de chaves."

        # {'nome': 'Aloma', 'Sobrenome': 'Barros', 'Ano': 1993}
        # {'nome': 'Aloma', 'Sobrenome': 'Barros', 'Ano': 1993}
        # {'nome': 'Aloma', 'Sobrenome': 'Barros', 'Ano': 1993}

  # print(dados1[dadosaloma]) - "O for percorre cada chave do dicionário, e ao usar dados1[dadosaloma], acessamos o valor correspondente a essa chave. Por isso, os valores são impressos um a um."

        # Aloma
        # Barros
        # 1993

    print(f"{dadosaloma} = {dados1[dadosaloma]}")

        # nome = Aloma
        # Sobrenome = Barros
        # Ano = 1993