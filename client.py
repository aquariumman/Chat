import socket, threading, time

key = 8194

shutdown = False
join = False

def receiving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                #print(data.decode('utf-8'))

                decrypt = ''
                k = False
                for i in data.decode('utf-8'):
                    if i ==':':
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                print(decrypt)

                time.sleep(0.3)

        except:
            pass#print('!!!Somthin wrong with receiving a message!!!')

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ('192.168.0.101', 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input('Enter your alias: ')

rT = threading.Thread(target=receiving, args=('RecvThread', s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(('['+alias + '] => join chat ').encode('utf-8'),server)
        join = True
    else:
        try:
            message = input()

            crypt = ''
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt

            if message != '':
                s.sendto(('['+alias + '] <= left chat ').encode('utf-8'),server)
                shutdown = True

rT.join(1)
s.close()

