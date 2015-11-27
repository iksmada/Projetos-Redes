#Servidor, responde requisicoes

import socket
import sys

def Servidor(args):
    #recebe a porta pela linha de comando
    port = args[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    pacote = ""
    '''
    pacote[0:4]   : Numero de sequencia (Aleatorio) 4 bytes
    pacote[5:9]   : ACK = 1+numero_seq_recebido     4 bytes
    pacote[10:15] : Checksum                        5 bytes
    pocate[15:]   : Data                            20 bytes

    total bytes:                                    33 bytes
    '''

    while 1:
        msg, addr = RecebePacote(s.recvfrom(33))
        envioCorreto = VerificaPacote(msg)
        EnviaPacote(msg)
        data, addr = s.recvfrom(33)
        print data
        s.sendto(pacote, (addr, port))

def RecebePacote(msg):
    ''' recebe o pacote e separa os dados recebidos '''
    data, addr = msg
    msg = []
    msg.append(data[0:4])
    msg.append(data[5:9])
    msg.append(data[10:15])
    msg.append(data[15:])
    return msg, addr

def VerificaPacote(msg):
    ''' Verifica se o checksum e ack recebidos estao correstos, retorna 1 pra sim e 0 pra nao '''
    pass

def EnviaPacote(msg):
    ''' Coloca a mensagem e o cabeçalho no formato certo e envia '''
    pass

def CalculaChecksum(numeroSquencia, ack):
    ''' Calcula checksum somando o numero de sequencia com o ack '''
    return str( int(numeroSequencia) + int(ack))

if __name__ == "__main__":
    Servidor(sys.argv)
