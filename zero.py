# Atribui a quantidade de inputs que ocorrerão à uma variável
qtd = int(input())
# Cria uma lista com os números que o chefe vai falar
numeros = []
# Cria um loop para receber essa quantidade de valores
for i in range(qtd):
    n = int(input())
    # Adiciona o número à lista caso ele não seja 0
    if n != 0:
        numeros.append(n)
    # Remove o último elemento da lista caso o input seja 0
    else:
        numeros.pop()
# Imprime a soma dos elementos do array
print(sum(numeros))
