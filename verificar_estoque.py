# Você trabalha em uma loja de ótica. Sua tarefa é codificar um programa que verifica se há óculos suficientes no estoque. 
# A função check_stock recebe uma lista eyeglasses como parâmetro e tem uma variável in_stock que é inicialmente definida como False.
# Se o número de óculos for maior ou igual a 5, defina in_stock como True e imprima a mensagem "Eyeglasses in stock".

# Caso contrário, imprima a mensagem "Out of stock".

# Retorne a variável in_stock da função.

def check_stock(eyeglasses):
    in_stock = False

    if len(eyeglasses) >= 5:
        in_stock = True
        print("Eyeglasses in stock")
    else:
        print("Out of stock") 

    return in_stock    