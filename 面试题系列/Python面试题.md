---
layout: 'false'
title: Python面试题
date: 2020-04-27 21:11:12
tags: 练习
---
1. 一行代码实现1-100之和
```
sum(range(100))
```

2. 如何在一个函数内部修改全局变量
```
In [1]: c = 0
In [3]: def change_count():
   ...:     global c
   ...:     c = 1
   ...:     print(c)
   ...:

In [4]: change_count()
1

In [5]: c
Out[5]: 1
```


3. 列出5个python标准库
os: 提供操作系统有关的函数
sys: 通常用于命令行参数
re: 正则匹配
math: 数学运算
datetime： 处理日期时间


4. 字典如何删除键和合并两个字典
删除：
```
del dic['key']
```

合并：
```
In [1]: dic1 = {"name":"ls"}

In [2]: dic2 = {"age":18}

In [3]: dic1.update(dic2)

In [4]: dic1
Out[4]: {'name': 'ls', 'age': 18}
```


5. 谈下python的GIL



6. python实现列表去重方法
字典法：
```
In [9]: old_list = [1,2,3,4,1,2,3]
In [11]: new_list = {}.fromkeys(old_list).keys()

In [12]: new_list
Out[12]: dict_keys([1, 2, 3, 4])
```

set方法
```
In [16]: old_list = [1,2,3,4,1,2,3]

In [17]: new_list = list(set(old_list))

In [18]: new_list
Out[18]: [1, 2, 3, 4]
```

7. `fun(*args, **kwargs)`中的 `*args、**kwargs`是什么?
`*args`是可变的positional arguments列表，
`**kwargs`是可变的keyword arguments列表
对于函数，前者指的是传入可变数量的参数列表，后者指的是可变数量的键值列表
```
def test_kwargs(first, *args, **kwargs):
   print 'Required argument: ', first
   for v in args:
      print 'Optional argument (*args): ', v
   for k, v in kwargs.items():
      print 'Optional argument %s (*kwargs): %s' % (k, v)

test_kwargs(1, 2, 3, 4, k1=5, k2=6)
# results:
# Required argument:  1
# Optional argument (*args):  2
# Optional argument (*args):  3
# Optional argument (*args):  4
# Optional argument k2 (*kwargs): 6
# Optional argument k1 (*kwargs): 5
```



8. 迭代器和生成器的区别？迭代器与列表的区别？
每个生成器都是迭代器，但是迭代器不一定是生成器。
它与列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算（lazy evaluation）方式返回元素，这正是它的优点。比如列表含有中一千万个整数，需要占超过400M的内存，而迭代器只需要几十个字节的空间。因为它并没有把所有元素装载到内存中，而是等到调用 next 方法时候才返回该元素。

生成器与迭代器基本特性相同，也是延迟计算方式返回元素，最大的区别是实现方式会比迭代器更加简洁。
```
In [1]: def func(n):
   ...:     yield n*2

In [2]: next(func(5))
Out[2]: 10
```
这种就是生成器函数，它用关键字yield返回。
生成器还有另外一种形式：
生成器表达式，和列表推导式很相似：
```
In [7]: sq = [x**2 for x in range(5)]

In [8]: sq
Out[8]: [0, 1, 4, 9, 16]
# 这个是列表推导式

In [12]: next(sq2)
Out[12]: 0

In [13]: next(sq2)
Out[13]: 1

In [14]: next(sq2)
Out[14]: 4

In [15]: next(sq2)
Out[15]: 9
```
迭代器和生成器只能被遍历一次，

9. 一句话解释什么样的语言能够用装饰器
可以将函数作为参数来传递的语言能够用装饰器


10. python数据类型有哪些？
int,list,bool,str,tuple,dict


11. 简述面向对象中__new__和__init__的区别
 `__init__`是初始化函数，对象被创建后会自动调用
 `__new__`会创建当前类的实例，并且自动调用`__init__`


12. 简述with方法打开文件帮我们处理了什么？
在处理文件过程中
```
f=open("./1.txt", "wb")
try:
    f.write("hello world")
except:
    pass
finally:
    f.close()
```

13. 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25],并使用列表推导式提取出大于10的数，最终输出[16,25]
```
In [1]: t = map(lambda x: x**2, [1,2,3,4,5])
In [2]: res = [i for i in t if i > 10]
In [3]: res
Out[3]: [16, 25]
```

14. python中生成随机整数、随机小数、0-1之间小数方法
```
In [4]: import random

In [5]: random.randint(0,10)  # 生成0-10中随机整数
Out[5]: 3

In [6]: random.random()  # 0-1随机数
Out[6]: 0.8382210808877724
```

15. 避免转义给字符串加哪个字母表示原始字符串
r, 表示需要原始字符串


16. `<div class="nam">中国</div>`,用正则匹配出标签里的内容（“中国”）,其中class的类名是不确定的
```
In [7]: import re

In [8]: str1 = '<div class="nam">中国</div>'

In [9]: res = re.findall(r'<div class=".*">(.*?)</div>',str1)

In [10]: print(res)
['中国']
```


17. python中断言方法举例
```
a = 3
assert(a>0)
```

18. 数据表student有id,name,score,city字段，其中name的名字可有重复，需要消除重复行，请写sql语句
```
SELECT DISTINCT name FROM student
```

19. 举例10个linux常用命令
`cd mkdir ls touch cat echo rm mv `


20. python2和python3的区别
 * range(1,5): python2返回列表，python3返回迭代器
 * python2中打印 `print "123"`, python3 `print("123")`
 * python2使用ascII编码，python3使用utf-8编码
