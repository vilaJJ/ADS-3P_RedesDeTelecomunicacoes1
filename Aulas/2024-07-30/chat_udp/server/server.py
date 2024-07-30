'''
Instituto Federal do Tocantins - IFTO Campus Araguaína
30 de julho de 2024 (2024-07-30), terça-feira
Curso: Análise e Desenvolvimento de Sistemas (CST)
Estudante: Juan Felipe Alves Flores             Período: 3°
Professor: Alexandre Cotrim Vilas Boas          Disciplina: Redes de Computadores I
'''

# Programa servidor - Chat UDP

import socket, pickle

ipServidor = "10.113.60.202"
portaServidor = 9090
buffer = 1024
 
socketServidor = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

socketServidor.bind((ipServidor, portaServidor))

print(f"Servidor UDP rodando\nEm {ipServidor}:{portaServidor}...")

while(True):
    bytesRecebidos = socketServidor.recvfrom(buffer)

    mensagemCliente = pickle.loads(bytesRecebidos[0])
    enderecoCliente = bytesRecebidos[1]

    mensagemCliente = f"Mensagem do cliente: '{mensagemCliente}'."
    ipCliente  = f"IP do cliente: {enderecoCliente}"

    print(f"{mensagemCliente} {ipCliente}")

    # Enviando retorno para o cliente

    mensagemParaCliente = f"Olá! A mensagem '{mensagemCliente}' foi recebida pelo servidor."
    bytesMensagemParaCliente = str.encode(mensagemParaCliente)

    socketServidor.sendto(bytesMensagemParaCliente, enderecoCliente)