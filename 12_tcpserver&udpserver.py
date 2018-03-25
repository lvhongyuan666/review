# tcp服务器


'''

import socket
# 1、创建一个socket套接字对象
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、bind 绑定IP和端口
address = ('', 7000)
server_sock.bind(address)

# 3、让服务器socket开启监听，等待客户端的连接请求
server_sock.listen(100)  # 参数表示允许连接的客户端的数量

# 4、accept 等待客户端的连接
client_sock, client_adddr = server_sock.accept()
print('客户端%s：进行了连接！' %client_adddr)


# 5、recv/send 接收发送数据
# recv()方法可以接收客户端发送过来的数据，指明最大收取1024个字节的数据
recv_date = client_sock.recv(1024)
# recv_date 接收的数据为bytes类型
print('接收的数据为：%s'%recv_date.decode())

# send()想客户端发送数据，要求发送的bytes类型的的数据
client_sock.send('thanks'.encode())

# 6、关闭连接
# 关闭与客户端的连接，
client_sock.close()
# 关闭服务器端的socket，关闭后，将不再接收任何客户端的连接
server_sock.close()
'''


'''
1、创建一个socket套接字对象
2、bind 绑定IP和端口
3、让服务器socket开启监听，等待客户端的连接请求
4、accept 等待客户端的连接
5、recv/send 接收发送数据
6、关闭连接
'''

'''

# 单进程服务器  -- 简单的tcp服务器
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 重复使用绑定的信息
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ('', 7999)
server_sock.bind(address)

server_sock.listen(100)

while True:
    print('---主进程，等待客户端的到来---')
    client_sock, client_addr = server_sock.accept()

    print('-----主进程，处理数据---%s' %str(client_addr))

    while True:
        recv_data = client_sock.recv(1024)
        if len(recv_data) >0:
            print('recv[%s]:%s' % (str(client_addr), recv_data.decode()))
        else:
            print('[%s]客户端已经关闭' % str(client_addr))
            break
    client_sock.close()

server_sock.close()
'''

'''

# 多进程tcp服务器
import socket
from multiprocessing import Process

def handle_client(client_sock, client_addr):
    while True:
        recv_data = client_sock.recv(1024)
        if len(recv_data) > 0:
            print('recv[%s]:%s' % (str(client_addr), recv_data.decode()))
        else:
            print('[%s]客户端已经关闭' % str(client_addr))
            break

    client_sock.close()


def main():

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    address = ('', 8000)
    server_sock.bind(address)
    server_sock.listen(100)

    while True:
        print('-----主进程，，等待新客户端的到来------')
        client_sock, client_addr = server_sock.accept()

        print('---接下来创建新的进程处理数据---%s' %str(client_addr))
        process = Process(target=handle_client, args=(client_sock,client_addr))
        process.start()
        # 因为每次有客户端连接，都会创建新的socket对象，每次负责处理一个客户端，处理完成后，占用较大内存，需要关闭
        client_sock.close()

if __name__ == '__main__':
    main()

'''

# 多线程的tcp服务器

import socket
from threading import Thread

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ('', 8000)
server_sock.bind(address)
server_sock.listen(100)

def handle_client(client_sock, client_addr):
    while True:
        recv_data = client_sock.recv(1024)
        if len(recv_data) > 0:
            print('recv[%s]:%s' % (str(client_addr), recv_data.decode()))
        else:
            print('[%s]客户端已经关闭' % str(client_addr))
            break

    client_sock.close()

def main():

    while True:
        print('-----主进程，，等待新客户端的到来------')
        client_sock, client_addr = server_sock.accept()

        print('---接下来创建新的线程处理数据---%s' % str(client_addr))
        t = Thread(target=handle_client, args=(client_sock, client_addr))
        t.start()
        # 因为多线程，共享进程内的资源，所以不能关闭
        # client_sock.close()

if __name__ == '__main__':
    main()



