import socket
import threading


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5055
address = (ip, port)

try:
    tcp.bind(address)
    tcp.listen(1)
    print("\033[01;32mServidor em escuta\033[0m")
    print(f"\033[01;32mPorta {port} conectada com sucesso!!\033[0m")
    from configs import receive_message, send_message
except OSError:
    print("\033[01;31mEssa porta já está em uso\033[0m")
    print("\033[01;31mImpossivel se conectar\033[0m")
    exit(0)
print("\033[01;33mDigite seu nome\033[0m")
nome = str(input("==> ")).lower()
try:
    while True:
        session, client_ip  = tcp.accept()
        if client_ip:
            print(f"\033[01;32m{client_ip[0]} conectado ao servidor\033[0m")

        enviar = threading.Thread(target=send_message, args=(session, nome))
        enviar.start()
        receber = threading.Thread(target=receive_message, args=(session,))
        receber.start()

except KeyboardInterrupt:
    print("\033[01;31mPrograma Interrompido\033[0m")
