'''
海哥的复习资料整理
'''

'''
1、从一个浏览器输入网址（url）到显示页面，中间都经历那些？
eg: www.baidu.com  ----域名
①客户端通过本机向访问DNS服务器
②DNS域名解析服务器解析域名并向客户端返回ip地址
③客户端通过ip地址，向服务器发送http请求（请求报文）
④服务器收到http请求后返回响应（响应报文）

网络层级--4层模型
应用层（http协议）--- 第四层
传输层（tcp、udp协议）
网络层
链路层  ---第一层（最外层）


服务器：--- tcp服务器（web服务器）+框架程序
接收请求报文，按照http协议进行解析 然后在按照WSGI协议将解析后的数据变成一个字典对象
然后将字典对象传给框架程序（django），由框架程序进行路由分发，寻找试图函数
将视图函数的处理结果交给服务器
服务器将处理结果封装为http响应报文， 返回给客户端


managy.py run  测试服务器

nginx 高性能的静态文件服务器 -- 提供静态文件能力强

购物车中的数据，对于断电的情况
1、没有致命的影响，对用户造成的影响不会大
2、redis持久化  -- 定时将内存中的数据写到磁盘中， 默认已经开启，可以设计持久化时间
但是在持久化的过程中，会丢失数据

购物车中数据保存哈希类型
原因：保存购物车中数据，不仅要保存商品的id，还要保存相对应的数量
{u_id : {sku_1: 10}, {sku_2: 2}}


http请求报文包含（起始行、请求头、请求体）
请求头包含哪些内容
accept： 浏览器可接受的文件格式，可以根据它来判断并返回适当的文件格式
Content-Type：请求的内容类型
Connection：keep-alive 用来告诉告诉服务器保持连接
Accept-Encoding：浏览器可接受的编码方式
Accept-Language：浏览器可接受的语言种类
cookie：浏览器用这个属性像服务器发送cookie


http和https的区别
http是超文本传输协议，信息是明文传输
https则是具有安全性的ssl加密传输协议

https是http协议和ssl构建的加密可进行加密传输、身份认证的网络协议

区别
1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用
2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议
3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后再是443
4、http的连接很简单，是无状态的;https是ssl协议+http协议构建的可进行加密传输、身份认证的网络协议，闭http协议安全


ssl协议是对http协议传输的数据进行加密

使用https方式和web服务器通信时的步骤
1、客户使用https的url访问web服务器，要求于web服务器建立ssl连接
2、web服务器收到客户端请求后，将网站的证书信息（证书中包含公钥）传送一份给客户端
3、浏览器根据与服务器协商的安全等级，建立会话密钥，利用网站的公钥将会话加密，并传送给网站
4、web服务器利用私钥解密出会话密钥

https优点：
防止数据在传输过程中不被窃取，改变、确保数据的完整性
缺点：
https协议在握手阶段比较费时（因为有加密、解密的过程），会使页面的加载时间延长
https连接缓存不如http高效、会增加数据开销和功耗








'''

'''
响应状态码 -- 告诉客户端，服务器的响应状态
200 ok  响应成功
201 Greated 响应已被创建

301 永久重定向
302 临时重定向

400 bad request 错误的请求
401 请求未被认证
403 fibiden 请求被禁止
404 not fund 找不到网页

500 internal server error 服务器内部错误
501 服务器暂不支持请求功能
502 bad gateway 充当网管或代理的服务器，从远端服务器接收到一个无效的请求

url 资源描述符    一个url对应一个网络上的资源
http的不同请求，对应资源的不同操作方式

http请求方式
GET 客户端从服务器获取数据 -- 获取页面信息   （查）
POST 客户端向服务器提交数据（提交表单或者上传文件）数据包含在请求体中 ---导致资源的建立或者修改 （增）
PUT  客户端向服务器传送的数据取代指定的文档的内容  （改）
DELETE 客户端指定服务器删除指定页面 （删）

GET和POST方式的区别
①原理
GET方式获取的信息，安全的，幂等的 仅获取信息，不会改变资源状态
幂等的： 对同一url的多个请求，返回同样的结果
POST方式会改变服务器上的资源

②表面
GET 请求的数据（参数）会附在url之后，以？分割 url和传输数据，以&相连，GET传递的数据直接暴露在浏览器的地址栏，缺乏安全性
POST提交的数据放在请求体中，安全性相对较高

GET方式提交的数据最多只能是1024字节，主要是受到url长度限制，而POST没有限制


'''




