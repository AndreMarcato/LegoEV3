import random
import matplotlib.pyplot as plt
import bluetooth

MAC = ''

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((MAC,1))
sock.send(b'Solicitar arquivo')
path = 'teste.log'
num_linhas = 100
with open(path, 'w') as arquivo:
    # Define o valor inicial do tempo
    tempo_anterior = 0
    # Escreve os dados de cada linha
    for _ in range(num_linhas):
        # Gera um valor de tempo aleatório maior que o anterior
        tempo = tempo_anterior + random.uniform(0, 1)
        # Gera outros números aleatórios para cada coluna
        erro = random.uniform(0, 10)
        P = random.uniform(0, 5)
        I = random.uniform(0, 3)
        U = P + I
        # Escreve os dados no arquivo de log
        arquivo.write(f'{tempo} {erro} {P} {I} {U}\n')
        # Atualiza o valor anterior do tempo
        tempo_anterior = tempo
        
t = []
erro = []
P = []
I = []
U = []

with open(path,'r') as arquivo:
    
    for linha in arquivo:
        
        dados = linha.split()
        
        t.append(float(dados[0]))
        erro.append(float(dados[1]))
        P.append(float(dados[2]))
        I.append(float(dados[3]))
        U.append(float(dados[4]))
        
        
plt.plot(t, erro, label='Erro')
plt.plot(t, P, label='P')
plt.plot(t, I, label='I')
plt.plot(t, U, label='U')
plt.xlabel('Tempo')
plt.ylabel('Valores')
plt.title('Gráfico dos Dados do Arquivo de Log')
plt.legend()
plt.show()