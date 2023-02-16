# Lista para guardar os resultados das partidas
resultados = []

# Recebe os 6 inputs e adiciona no array de resultados
for i in range(6):
    partida = input()
    resultados.append(partida)

# Conta as vitórias e derrotas no array
vitorias = resultados.count("v")
derrotas = resultados.count("p")

# Separa os participantes por grupo baseado na quantidade de vitórias
if vitorias >= 5:
    print(1)
elif vitorias >= 3:
    print(2)
elif vitorias >= 1:
    print(3)
else:
    print(-1)
