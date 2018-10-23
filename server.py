import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket.AF_INET -- TCP, socket.SOCK_DGRAM -- IP
s.bind((host, port))  # creation TCP/IP

quit = False
print('=== SERVER STARTED ===')

while not quit:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        itsatime = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())

        print('[' + addr[0] + ']=[' + str(addr[1]) + ']=[' + itsatime + ']/', end='')
        print(data.decode('utf-8'))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print('\n\n\n=== Server Stoped ===')
        quit = True

s.close()


