'''
网路编程
'''
'''
网络是一种通讯工具，可以把数据从一方传递给另外一方

网络编程就是让不同的电脑上的软件能够进行数据传递，即：进程间的通信

'''

'''
网络层级模型 tcp/ip模型
tcp/ip协议
link/internet/transport/application
层与层相互协作的时候，数据在经历不同的网络层级的时候，会有数据的打包与解包工作

协议：
我们想让网络通讯的每一层在工作时，都能按照其相应的某一种具体的工作流程来工作，比如具体的规章制度、规则、工作的标准，我们就需要制定出这些规则标准，这就是我们所说的不同网络层中的协议
'''

'''
UDP--用户数据报协议

是一个无连接的简单的面向数据报的协议
无连接：在通讯前，不需要连接就可以用来发送和接收消息

优点：传输效率高
缺点：不可靠
它只是把应用程序传给IP层的数据报发送出去，但是并不能保证它们能到达目的地
应用场景：
语音广播
视频
qq
DNS（域名解析）
'''


'''
socket---网络通讯的工具

python中socket模块中的socket类可以完成

socket.socket(AddressFamily, Type)
函数 socket.socket 创建一个 socket，返回该 socket 的描述符，该函数带有两个参数：

Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
'''


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# print('Socket Created')


'''
TCP-- 传输控制协议
是一个面向连接的、可靠的、基于字节流的传输控制协议

tcp通讯需要经过三个步骤：创建连接、数据传输、终止连接

tcp的三个特点的分析
①面向连接：通信双方必须建立连接才能进行数据的传输，数据交换完成后，双方必须断开此连接，以释放系统资源
②基于数据流（字节流）：
tcp会把数据流切分成一个或多个适当长度的报文段发出去
udp则把它封装成一个udp数据报发送出去，如果用户没有足够的缓冲区来读取数据包，则udp数据报就会被截断
③可靠传输：
发送应答机制
超时重传机制
错误校验
流量控制与阻塞管理

三次握手
SYN--->
        <---ACK/SYN
ACK---->
四次挥手
FIN\ACK---->
        <----ACK
        <----ACK/FIN
ACK----->
由于TCP连接是可以双向通信的（全双工），因此每个方向都必须单独进行关闭


tcp长连接、短连接
长： 建立连接---数据传输---关闭连接
短：建立连接---数据传输（保持连接）---关闭连接

优缺点：
长连接可以省去较多的TCP建立和关闭的操作，减少浪费，节约时间。

对于频繁请求资源的客户来说，较适用长连接。

client与server之间的连接如果一直不关闭的话，会存在一个问题，

随着客户端连接越来越多，server早晚有扛不住的时候，这时候server端需要采取一些策略，

如关闭一些长时间没有读写事件发生的连接，这样可以避免一些恶意连接导致server端服务受损；

如果条件再允许就可以以客户端机器为颗粒度，限制每个客户端的最大长连接数

短连接对于服务器来说管理较为简单，存在的连接都是有用的连接，不需要额外的控制手段。
但如果客户请求频繁，将在TCP的建立和关闭操作上浪费时间和带宽

应用场景：
长：多用于操作频繁、点对点的通讯、而且连接数不能太多
短：像web网站的http服务，一般都用短连接，因为长连接对于服务端会耗费一定的资源
而web网站这么频繁的访问量，短连接会更省资源
'''


'''
协程-- 又称微线程

协程是比线程更小的执行单元，自带cup上下文

进程、线程、协程都是进行多任务处理的

理解协程：
每个线程里面有多个函数，eg：函数1、函数2，我们让函数1和函数2交替去运行，我们可以把函数1和函数2理解为2个协程
协作相互配合执行

协程是程序员在设计的时候自己划分出来的解决方案

在python中，使用yield关键字实现协程
'''
# 协程案例,使用yield的关键字使两个函数交替运行，实现协程

import time


def A():
    while True:
        print('---A---')
        yield
        time.sleep(0.5)


def B(c):
    while True:
        print('---B---')
        c.__next__()
        time.sleep(0.5)

# if __name__ == '__main__':
#     a = A()
#     B(a)

'''
协程的关键字yield和next关键字被封装在greenlet库里
只使用swich（）方法
'''
from greenlet import greenlet
import time

def C():
    while True:
        print('---C---')
        gr2.switch()
        time.sleep(0.5)

def D():
    while True:
        print('---D---')

        gr1.switch()
        time.sleep(0.5)

# 创建两个协程对象
gr1 = greenlet(C)
gr2 = greenlet(D)

gr1.switch()


'''
gevent库是对greenlet库的进一步封装

gevent库相当在线程中新建一个主函数，有主函数去切换
由gevent库切换，当协程中发生阻塞时候，主函数会自动切换
'''

# 例子

import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)  # 打印当前协程的id
        gevent.sleep(0.1)  # 让函数发生阻塞，主函数会自动切换协程

# 创建三个携程对象
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()



