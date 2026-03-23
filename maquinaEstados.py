import random
import time
import subprocess

def gerar_trafego(bitrate):
    cmd = [
        "sudo", "himage",
        "pc1", "iperf",
        "-c", "10.0.0.20",
        "-u",
        "-b", bitrate,
        "-l", "1400"
        "-t", "5",
        "-y", "C"
    ]
    
    subprocess.run(cmd)  # bloqueia até terminar

estados = ["Ocioso", "TrafMed", "TrafAlt"]

def tratador_Ocioso():
    sleep(5)
    
def tratador_TrafMed():
    gerar_trafego("10M")
    
def tratador_TrafAlt():
    gerar_trafego("50M")

# matriz de transição
transicao = {
    "Ocioso":  [0.6, 0.3, 0.1],
    "TrafMed": [0.2, 0.6, 0.2],
    "TrafAlt": [0.1, 0.3, 0.6],
}

    
def prox_estado(current):
    probabilidades = transicao[current]
    return random.choices(estados, probabilidades)[0]

estado = "Ocioso"

while True:
    print(f"Estado atual: {estado}")
    time.sleep(0.4)
    estado = prox_estado(estado)