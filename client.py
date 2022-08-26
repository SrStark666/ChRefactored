import socket
import threading
from configs import receive_message, send_message


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("127.0.0.1", 5055)

tcp.connect(address)
print(f"\033[01;32mConectado ao servidor\033[0m")
print("\033[01;33mDigite seu nome\033[0m")
nome = str(input("==> ")).lower()
if __name__ == "__main__":
    enviar = threading.Thread(target=send_message, args=(tcp, nome))
    enviar.start()
    receber = threading.Thread(target=receive_message, args=(tcp,))
    receber.start()