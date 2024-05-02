import random
import matplotlib.pyplot as plt
import paramiko, pandas as pd

hostname = 'ev3dev.local'
port = 22
username = 'robot'
password = 'maker'  # Se necessário

diretorio_ev3 = '/home/robot/'

cliente_ssh = paramiko.SSHClient()
cliente_ssh.load_system_host_keys()
cliente_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

cliente_ssh.connect(hostname, port, username, password)

stdin, stdout, stderr = cliente_ssh.exec_command(f'ls {diretorio_ev3}')

# Leia a saída do comando e obtenha a lista de arquivos
arquivos = stdout.read().decode('utf-8').splitlines()

# Crie um menu com as opções de cada arquivo
print("Escolha um arquivo:")
for i, arquivo in enumerate(arquivos):
    print(f"{i+1}. {arquivo}")

# Leia a opção do usuário
opcao = int(input("Digite o número do arquivo que deseja ler: "))
path = diretorio_ev3+arquivos[opcao - 1]
print(path)

stdin, stdout, stderr = cliente_ssh.exec_command(f'cat {path}')


with cliente_ssh.open_sftp() as sftp:
        with sftp.open(path) as file:
            # Lendo o conteúdo do arquivo e ignorando a primeira linha
            df = pd.read_csv(file)
print(df)
# Definindo a coluna "tempo" como o índice do DataFrame
df.set_index('Tempo', inplace=True)

# Plotando os dados do DataFrame
df.plot()
plt.xlabel('Tempo')
plt.ylabel('Valores')
plt.title('Gráfico dos Dados do Arquivo de Log')
plt.legend(title='Amostra')
plt.show()             

# plt.plot(df['tempo'], erro, label='Erro')
# plt.plot(t, P, label='P')
# plt.plot(t, I, label='I')
# plt.plot(t, U, label='U')
# plt.xlabel('Tempo')
# plt.ylabel('Valores')
# plt.title('Gráfico dos Dados do Arquivo de Log')
# plt.legend()
# plt.show()