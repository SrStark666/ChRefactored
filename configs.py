def receive_message(tcp):
    while True:
        try:
            package = tcp.recv(1024).decode("utf-8")
        except KeyboardInterrupt:
            break
        if package:
            print(package)
        elif package == "sair" or package == "exit":
            tcp.close()
            exit(0)
        elif not package:
            continue

def send_message(tcp, nome):
    while True:
        msg = str(input(f"\033[01;32m[{nome}]: \033[0m"))
        if msg == "/exit":
            tcp.close()
            break
        msg = (f"[{nome}]:" + msg)
        tcp.send(bytes(msg, encoding="utf-8"))
        