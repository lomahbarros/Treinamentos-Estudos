# Você está construindo uma aplicação web para um restaurante que calcula o preço total de um item após o imposto.
# Complete a função calculate_tax que recebe um preço específico e o atualiza com um imposto adicionado de 10%.
# Certifique-se de retornar o price atualizado após o cálculo.

def calculate_tax(price):
    price += price * 0.1
    return price

while True:

    price = float(input("Digite o valor do produto: "))
    preco_com_imposto = calculate_tax(price)


    print(preco_com_imposto)