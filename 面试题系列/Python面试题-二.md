---
layout: 'false'
title: Python面试题(二)
date: 2020-05-02 10:27:26
tags:
---
21. 列出python中可变数据类型和不可变数据类型，并简述原理
**不可变类型：字符串str, 数值类型int, 元组tuple**
```
In [1]: a = 3

In [2]: b = 3

In [3]: id(a)
Out[3]: 4494963920

In [4]: id(b)
Out[4]: 4494963920
```
不可变类型指的是数据不允许放生变化，如果改变变量的值就只能重新创建新的对象会重新分配内存地址，所以它的id将会有所改变。

```
In [5]: a = 4

In [6]: id(a)
Out[6]: 4494963952
```

**可变类型：列表list和字典dict**
也就是说如果对变量进行append、 +=等操作它只会改变变量的值，不会改变内存地址。对于相同值的不同对象也会占用不同的内存地址。
```
In [7]: a = [1,2]

In [8]: id(a)
Out[8]: 4530984192

In [9]: b=[1,2]

In [10]: id(b)
Out[10]: 4530973424

In [13]: b.append(3)

In [14]: b
Out[14]: [1, 2, 3]

In [15]: id(b)
Out[15]: 4530973424
```


22. s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
```
In [1]: s = "ajldjlajfdljfddd"

In [2]: s = set(s)

In [4]: s = list(s)

In [5]: s.sort(reverse=False)

In [6]: res = "".join(s)

In [7]: res
Out[7]: 'adfjl'
```

23. 用lambda函数实现两个数相乘
```
In [8]: sums = lambda a,b:a*b
In [9]: sums(1,2)
Out[9]: 2
```

24. 字典根据键从小到大排序
```
In [10]: dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
In [12]: lis = sorted(dic.items(), key=lambda i:i[0], reverse=False)
In [13]: lis
Out[13]: [('age', 18), ('city', '深圳'), ('name', 'zs'), ('tel', '1362626627')]

In [15]: dict(lis)
Out[15]: {'age': 18, 'city': '深圳', 'name': 'zs', 'tel': '1362626627'}
```

25. 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
```
In [1]: from collections import Counter

In [2]: a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

In [3]: res = Counter(a)

In [4]: res
Out[4]:
Counter({'k': 1,
         'j': 3,
         'a': 4,
         'l': 9,
         'f': 5,
         ';': 6,
         'd': 3,
         's': 2,
         'h': 6,
         'g': 1,
         'b': 1})
```


26. 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
```
In [4]: import re
In [5]: a = "not 404 found 张三 99 深圳"
In [6]: l = a.split(" ")
In [7]: res = re.findall('\d+|[A-Za-z]+',a)
In [8]: for i in res:
    ...:     if i in l:
    ...:         l.remove(i)
In [10]: print(" ".join(l))
    张三 深圳
```

27. filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
In [1]: a = [1,2,3,4,5,6,7,8,9,10]

In [2]: def fl(a):
   ...:     return a%2 == 1
   ...:

In [3]: newlist = filter(fl,a )

In [5]: newlist = [i for i in newlist]

In [6]: newlist
Out[6]: [1, 3, 5, 7, 9]
```


28. 列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
res = [i for i in a if i%2==1]
```

29. 正则re.complie作用
re.compile是将正则表达式编译成一个对象，加快速度，并重复使用


30. a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
分别是：tuple， int, str

31. 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,5,6,7,8,9]
```
In [18]: a.extend(b)

In [19]: a
Out[19]: [1, 5, 7, 9, 2, 2, 6, 8]
In [21]: a.sort(reverse=False)

In [22]: a
Out[22]: [1, 2, 2, 5, 6, 7, 8, 9]
```

32. 用python删除文件和用linux命令删除文件方法
python: os.remvoe(file)
linux: rm file


33. log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
```
In [23]: import datetime

In [28]: a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

In [29]: a
Out[29]: '2020-05-04 23:02:46'
```


34. 数据库优化查询方法
索引：
使用中间表，外链：


35. 请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
matplotlib


36. 写一段自定义异常代码
```
In [30]: def fn():
    ...:     try:
    ...:         for i in range(5):
    ...:             if i > 2:
    ...:                 raise Exception("大于2")
    ...:     except Exception as ret:
    ...:         print(ret)
    ...:

In [31]: fn()
大于2
```

37. 正则表达式匹配中，`（.*）`和`（.*?）`匹配区别？
贪婪匹配：
```
In [32]: s="<a>标签1</a><a>标签2</a>"
In [35]: res1 = re.findall("<a>(.*)</a>",s)
In [37]: res1
Out[37]: ['标签1</a><a>标签2']
```
非贪婪匹配：
```
In [32]: s="<a>标签1</a><a>标签2</a>"
In [35]: res1 = re.findall("<a>(.*?)</a>",s)
In [37]: res1
Out[37]: ['标签1', '标签2']
```

38. 简述Django的orm
简单来说就是ORM相当于是面向对象的数据库语句，它的函数封装了mysql，oracle常用的增删改查功能，比如`save`就是数据库的insert或者update，getallObject就是select语句。
在Django中每个model映射为一个数据表，model中的每个属性都代表着数据表中的字段。


39. [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
```
In [49]: x = [j for i in a for j in i]
In [50]: x
Out[50]: [1, 2, 3, 4, 5,]
```

40. x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
```
In [51]: x = "abc"
In [53]: y="def"

In [54]: z=["d","e","f"]

In [55]: m = x.join(y)

In [56]: n = x.join(z)

In [57]: m
Out[57]: 'dabceabcf'

In [58]: n
Out[58]: 'dabceabcf'
```
join与os.path.join的区别：
join会将前x以分隔符的方式放入后者


41. 举例说明异常模块中try except else finally的相关意义


42. python中交换两个数值
```
In [59]: a,b=3,4

In [60]: a,b=b,a

In [61]: a
Out[61]: 4

In [62]: b
Out[62]: 3
```



43. 举例说明zip（）函数用法
zip函数会把一个或多个序列也就是可迭代对象作为参数返回一个元组的列表，同时将这些序列中并排的元素配对。
```
In [1]: a = [1,2]

In [2]: b=[3,4]

In [3]: res = [i for i in zip(a,b)]

In [4]: res
Out[4]: [(1, 3), (2, 4)]

In [5]: a="ab"

In [6]: b
Out[6]: [3, 4]

In [7]: b="xyz"

In [8]: res=[i for i in zip(a,b)]

In [9]: res
Out[9]: [('a', 'x'), ('b', 'y')]
```

44. a="张明 98分"，用re.sub，将98替换为100
```
In [1]: a = "张明 50分"

In [2]: import re

In [3]: res=re.sub(r'\d+',"100",a)

In [4]: res
Out[4]: '张明 100分'
```


45. 写5条常用sql语句
```
show databases;

show tables;

desc 表名;

select * from 表名;

delete from 表名 where id=5;

update students set gender=0,hometown="北京" where id=5
```

46. a="hello"和b="你好"编码成bytes类型


47. [1,2,3]+[4,5,6]的结果是多少？
等价于extend
```
[1,2,3,4,5,6]
```


48. 提高python运行效率的方法
 * 使用生成器或迭代器节约内存
 * 多线程，多进程
 * 优化算法
 * 循环优化

 49. 正则匹配日期2018-03-20
 url = https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462

```
res = re.findall(r'dateRange=(.*?)%7C(.*?)&',url)
In [12]: res
Out[12]: [('2018-03-20', '2018-03-20')]
```

52. list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
**快速排序**
```
def quicksort(list):
    if len(list) < 2:
        return list

    pivot = list[0]
    less = [i for i in list[1:] if i <= pivot]
    greater = [i for i in list[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
```

56. 列出常见的状态码和意义
200 请求正常
404 找不到资源
500 服务器故障
403 请求资源被拒绝

57. 后端优化
 * 合理使用缓存，比如缓存可以存储一些读写次数高不需要担心安全问题的，不怎么需要更改的数据
 * 异步
 * 算法优化，循环优化

 58. 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
 ```
 In [1]: dic={"name":"zs","age":18}

In [2]: dic.pop("name")
Out[2]: 'zs'

In [3]: dic
Out[3]: {'age': 18}

In [4]: del dic["age"]

In [5]: dic
Out[5]: {}
 ```

 59. 列出常见MYSQL数据存储引擎
 InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。


 60. Redis与MySQL的区别
 Redis:
 * 非关系型数据库，完全开源免费的key-value数据库。一个支持多种数据结构的数据库
 * 将数据存储在内存中，读写速度快
 * 数据持久化，重启后仍可继续使用
 * 支持多种数据结构:strings，set，sorted set，list

 61. 简述同源策略
 协议相同
 端口相同
 域名相同
 只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”

62. 简述cookie和session的区别

* cookie 安全性没session高
* cookie是用在客户端上的，session是来自于服务端
* session的session id依赖于cookie，需要存在cookie中，如果浏览器禁用了cookie，session也会失效

63. 简述线程与进程
进程好比是火车，线程则是火车车厢
* 一个进程可以有多个线程
* 进程与进程之间无任何关联
* 如果进程销毁了，它的所有线程也将消失
* 同一进程下不同线程可以共享数据，但是不同进程之间共享数据就很难
* 进程使用的内存地址可以上锁，只有其中一个线程使用完了才能给其他线程用。这可以称为互斥锁，也就是线程锁


66. python中copy和deepcopy区别
浅拷贝
仅拷贝对象，如果对象中还有其他元素，则不会做拷贝

深拷贝
不仅拷贝对象，对象中的元素（除了不可变元素）都会被拷贝

特殊情况
如果深拷贝对象是元组，



70. a = " hehheh ",去除首尾空格
 ```
 a.strip()
 ```

72. 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
```
In [46]: a = sorted(foo, reverse=False)
```

73. 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小

```
In [65]: a = sorted(foo, key=lambda x:(x<0, abs(x)))
```
小于0的按照绝对值大小进行排序

74. 列表嵌套字典的排序，分别根据年龄和姓名排序

foo = [{"name":"zs","age":19},{"name":"ll","age":54},

{"name":"wa","age":17},{"name":"df","age":23}]

```
In [70]: f = sorted(foo, key=lambda x:x["age"])
```

77. 根据键对字典排序（方法一，zip函数）
```
In [79]: s = sorted(dic.items(), key=lambda x:x[0])
Out[80]: [('city', 'beijing'), ('name', 'zs'), ('sex', 'man')]
```

81. 举例说明SQL注入和解决办法
当以字符串格式化书写方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行，比如例子中的SQL注入会删除数据库demo

sql预编译，
```
String sql = "select id, no from user where id=?";
PreparedStatement ps = conn.prepareStatement(sql);
ps.setInt(1, id);
ps.executeQuery();
```
参数校验：
不能带有特殊符号等格式问题，一般限制邮箱，手机号形式


82. s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']

```
In [16]: res = re.split(r':|\s',s)
```

83. 正则匹配以http://163.com结尾的邮箱
```
re.match("\w+@163.com$",str)
```

84. 递归求1-10的总和
```
def sums(num):
    if num > 0:
        res = num + sums(num-1)
    else:
        res = 0
    return res

print(sums(10))
```

86. MyISAM 与 InnoDB 区别：
 * MyISAM不支持事务，InnoDB支持事务，这也是MySQL默认引擎为InnoDB的最大原因
 * InnoDB支持外键
 * MyISAM支持全文本搜索，InnoDB不支持
 * MyISAM表保存成文件形式，跨平台使用更加方便

 * MyISAM管理非事务表，提供高速存储和检索以及全文搜索能力，如果再应用中执行大量select操作，应该选择MyISAM
 * InnoDB用于事务处理，具有ACID事务支持等特性，如果在应用中执行大量insert和update操作，应该选择InnoDB


 87. MySQL全文搜索与like的区别
 * like效率没有全文本高，随着文本的长度增加耗时也会随之增长
 * like无法控制匹配条件，哪些关键词无须匹配哪些需要过滤掉等情况
 * 全文本能做到智能化匹配结果，可以控制匹配结果的优先级，匹配一个或多个关键词
