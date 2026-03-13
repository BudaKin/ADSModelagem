import numpy as np

P = np.array([
[0.6,0.3,0.1],
[0.2,0.6,0.2],
[0.1,0.3,0.6]
])

taxa = np.array([0,10,50])

estado = 0
passos = 500
epoca = 5

trafego = []
estados_visitados = []

for i in range(passos):

    estados_visitados.append(estado)
    trafego.append(taxa[estado])

    estado = np.random.choice([0,1,2], p=P[estado])

tempo_total = passos * epoca

print("Tempo total:", tempo_total, "segundos")
print("Tráfego médio simulado:", np.mean(trafego), "Mbps")

contagem = np.bincount(estados_visitados, minlength=3)
pi_pratico = contagem / passos

print("Regime permanente prático:")
print(pi_pratico)