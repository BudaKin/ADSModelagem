import random
import time
import subprocess


class Estado:
    def __init__(self, nome, run, transicoes):
        self.nome = nome
        self.run = run
        self.transicoes = transicoes

    def prox_estado(self):
        estados = list(self.transicoes.keys())
        probabilidades = list(self.transicoes.values())
        return random.choices(estados, probabilidades)[0]


def gerar_trafego(bitrate):
    cmd = [
        "sudo","himage",
        "pc1","iperf",
        "-c","10.0.0.20",
        "-u",
        "-b", bitrate, 
        "-l", "1400",
        "-t", "5",
        "-y", "C",
    ]

    subprocess.run(cmd)  # bloqueia até terminar


# Tratadores dos estados
def tratador_Ocioso():
    time.sleep(5)


def tratador_TrafMed():
    gerar_trafego("10M")


def tratador_TrafAlt():
    gerar_trafego("50M")


# Definição dos Estados
ocioso = Estado("Ocioso", tratador_Ocioso, {})
trafMed = Estado("TrafMed", tratador_TrafMed, {})
trafAlt = Estado("TrafAlt", tratador_TrafAlt, {})

ocioso.transicoes = {ocioso: 0.6, trafMed: 0.3, trafAlt: 0.1}
trafMed.transicoes = {ocioso: 0.2, trafMed: 0.6, trafAlt: 0.2}
trafAlt.transicoes = {ocioso: 0.1, trafMed: 0.3, trafAlt: 0.6}

epocas = 50

# Estado inicial
estado = ocioso

# iperf servidor
cmd = [
    "sudo","himage",
    "pc2","iperf",
     "-s", "-u","-D"]

subprocess.run(cmd)

for _ in range(50):
    print(f"Estado atual: {estado.nome}")
    estado.run()
    estado = estado.prox_estado()
