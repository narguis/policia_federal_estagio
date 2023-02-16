# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# Variável para armazenar a soma
n = 0
# Loop para contar de 1 a 999 (Todos os naturais abaixo de 1000)
for i in range(1, 1000):
    # Checa se o número é múltiplo de 3 ou de 5
    if i % 3 == 0 or i % 5 == 0:
        # Adiciona o número na soma caso ele seja múltiplo
        n += i
# Mostra a soma na tela
print(n)
