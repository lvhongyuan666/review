'''
数据库的基本了解：

存储数据的仓库

优点：
①持久化存储
②读写速度极高
③保证数据的有效性

SQL
在数据库中进行操作的语句
'''

'''
 数据库的优化

 ①数据表的设计：
 准循三范式（每一个字段拆分到不能在拆分、每一条实力必须唯一标识，每一列不能依赖非主键）
 设计的时候要考虑到可能会用到的查询，为方便查询而设计，比如：用空间换时间，适当增加冗余字段，节省查询开销

 ②建立索引：主键、外键、唯一约束、普通索引（key/index）
 在where条件后经常出现的字段建立索引
 索引的使用：最左原则
 eg: select * from table where f1=xx and f2 = xxx
 要将有索引的字段放在前面


 ③sql语句的优化
 3.1使用索引，注意关键字的顺序，
 3.2 不要使用select *
 3.3 能使用联合查询，不使用嵌套（子查询）

联合查询-- select  from tbl_a a inner join tbl_b b on a.field=b.filed where b.=

子查询 -- select from tbl_a where filed=(select field from tbl_b where b.=)
子查询：一个select 语句中嵌入了另一个select语句

 3.4 使用分析工具分析效率低的sql语句 --工具：满查询工具

 ④使用缓存 redis mencached

 ⑤读写分离
 配置多个数据库 双机互备 -- （主负责写、改、增、删，  从负责 查）

 ⑥分表分库 水平分表，分库

'''

'''
mysql的查询
①条件
select * from table where 条件

使用where语句，对表中的数据进行筛选 where后面支持多种运算符
比较运算符： < > =  !=
逻辑运算符： and or not
模糊查询： like %表示任意多个字符  _ 表示任意一个字符
eg ：select * from students where name like '黄%'

范围查询： in 表示在一个非联系的范围内
eg ： 。。。。 where id in(1,3,5)

空判断： null
eg ：。。。 where height is not null  ------身高不为空的


优先级 由高到低
（） not 比较运算符 逻辑运算符
从高到低，not and or  --- 如果同时出现并希望or优先，要结合（）使用

② 排序
order by 列1  ----默认是升序
order by 列2 desc  是降序



③聚合函数 ： 快速统计数据

count（）
max（）
min（）
sum（）
avg（）

④分组 ---按照字段进行分组
通常与聚合函数一起使用
select 列1,列2,聚合... from 表名 group by 列1,列2...

eg : select sex,count(*) from author group by sex;
按照性别统计出人数（每个性别的人数）

⑤分页 -- 当数据量过大时，在一页中查看数据是非常麻烦的事
limit start，count
从start开始，获取count条数据

⑥连接查询
当查询结果来源于多张表的时候，需要将多张表连成一个大的数据集
内连接查询：查询的结果为两个表匹配到的数据
左连接查询：查询的结果为两个表匹配到的数据，左表特有的数据，对于右表中不存在的数据使用null填充
右连接查询：查询的结果为两个表匹配到的数据，右表特有的数据，对于左表中不存在的数据使用null填充


⑦自关联  -- 一张表上，存在这相互关系

⑧子查询  --- 一个select中套一个select ×

'''

'''
数据库高级
①存储过程：
翻译为存储程序，是一条或者多条SQL语句的集合


②视图
对于复杂的查询，在多个地方被使用，如果需求发生了改变，就需要更改sql语句，则需要在多个地方进行更改，维护起来非常麻烦

解决：视图
视图本质就是对查询的封装

就是将一个查询结果封装起来，用的时候直接使用


③ 事物 *****
事物的四大特性（简称ACID）
原子性 ： 事物的操作，要么全部成功，要么全部失败
一致性： 并行的事物，其执行顺序和执行结果是一致的
隔离性： 事物的执行，互不干扰
永久性 ：事物一旦执行完成，将永久保存

④索引 *******
提高查询速度，但降低更新表的速度，如对表进行INSERT、UPDATE和DELETE，因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件
建立索引会占用磁盘空间的索引文件

 show index from 表名  ---- 查看索引
 create index 索引名称 on 表名(字段名称(长度))  ---- 创建索引
 drop index 索引名称 on 表名  ---- 删除索引

'''
'''
NOSQL 非关系型数据库
优势：
①易扩展: nosql 的共同点就是数据之间没有关系，这样易于扩展
②大数据量，高性能：NoSql都具有非常高的读写性能，尤其在大数据量下，同样表现优先，得益于它的无关系性，数据库的结构简单
③灵活的数据模型：NoSQL无需事先为要存储的数据建立字段，随时可以存储自定义的数据格式
④高可用：NoSQL在不太影响性能的情况，就可以方便的实现高可用的架构

'''

'''
redis -- 是一个开源的，内存性的数据存储系统，它可以用做数据库，缓存和消息中间件

redis是key-value的数据结构，每一条数据都是一个键值对
键的类型是字符串，键不能重复
值的类型有五种：
字符串string
哈希hash
列表list
集合set
有序集合zset
'''


'''
字符串string --string类型是二进制安全的，可以存储任何数据，比如数字、图片等
设置
set key value
mset key1 value1 key2 value2
append key value

获取
get key
mget key1 key2 key3
'''

'''
hash 用于存储对象，对象的结构为属性、值
值得类型为string
设置
hset key field value
hmset key field1 value1 field2 value2

获取
hkeys key   --- 获取指定键的所有属性
hget key field  --- 获取一个属性的值
hvals key  --- 获取所有属性的值

删除
hdel key field1 field2

'''

'''
列表 list

增加
rpush key value1 value2 -- 从右边插入
lpush key value1 value2  -- 从左边插入

获取
lrange key start stop   --- start stop 指的是下标元素


'''

'''
set  -- 无序集合
元素具有唯一性

增肌
sadd key menber1 menber2

获取
smembers key

删除
srem key member -- 删除指定元素

'''

'''
zset  -- 有序集合  sorted set
每个元素都会关联一个double类型的score，表示权重，通过权重将元素从小到大排序

增加
zadd key score1 member1 score2 member2

获取
zrange key start stop

删除
zrem key member1 member2

'''