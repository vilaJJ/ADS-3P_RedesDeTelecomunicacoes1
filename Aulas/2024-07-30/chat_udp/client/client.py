'''
Instituto Federal do Tocantins - IFTO Campus Araguaína
30 de julho de 2024 (2024-07-30), terça-feira
Curso: Análise e Desenvolvimento de Sistemas (CST)
Estudante: Juan Felipe Alves Flores             Período: 3°
Professor: Alexandre Cotrim Vilas Boas          Disciplina: Redes de Computadores I
'''

# Programa cliente - Chat UDP

import socket, pickle

ipCliente = "10.113.60.202"
portaCliente = 9000
buffer = 1024

# Objeto do cliente socket para chat UDP
socketClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    ip = input("Insira o endereço do servidor: ")
    porta = int(input("Insira a porta do servidor: "))

    mensagem = input("\nInsira a mensagem que deseja enviar: ")
    mensagemData = pickle.dumps(mensagem)

    resultado = socketClient.sendto(mensagemData, (ip, porta))    
    mensagemServidor = socketClient.recvfrom(buffer)

    print(f"Resposta do servidor: {mensagemServidor[0].decode()}")
    print("\nComunicação realizada com sucesso.\n" + ("="*80))
