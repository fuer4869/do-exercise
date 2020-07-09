---
layout: 'false'
title: Python面试题四
date: 2020-05-28 11:27:40
tags:
---

42. Python中类方法、类实例方法、静态方法有何区别？
* 实例方法：类的实例化对象的方法，参数是`self`，指向该类的实例。通过self可以自由的调用该对象的属性和其它方法，也可以修改。
* 类方法：使用@classmethod装饰器的类方法，参数为`cls`，不同于实例方法，`cls`不能对类中的属性做修改
* 静态方法：使用@staticmethod装饰器的类方法，不接受`cls`和`self`，但是可以接受其它参数。所以它不能访问该类的属性和方法，只能访问该类中的全局变量。

[参考链接](https://geek-docs.com/python/python-examples/python-instance-methods-and-class-methods-and-reveal-the-static-method.html)

46. 请描述抽象类和接口类的区别和联系
举个简单的例子，你需要设计一个关于汽车的类。为了便于以后的扩展，我们把汽车的基本功能放入到抽象类中去，如行驶，倒车，转弯这些方法，车灯，轮胎等属性。
突然我们开发出了一台支持自动驾驶的车，因为这个功能不是每台车都有的所以就把这个功能设计到接口类中去。

* 抽象类类似于 is a的关系。定义该体系中基本共性内容，例子中车灯，行驶都是每辆车必备的功能
* 而接口类类似于 like a的关系。属于体系的额外功能，可能有可能没有。自动驾驶就不是每辆车都有的功能


[参考资料](https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p12_define_interface_or_abstract_base_class.html)
[参考资料](https://www.zhihu.com/question/20149818/answer/153188511)
[参考资料](https://juejin.im/post/5c0d4859e51d4504a02eb6e2)


53. 简述read、readline、readlines的区别？
read 读取整个文件
readline 读取下一行
readlines 读取整个文件到一个迭代器以供我们遍历

54. 写一个装饰器
```
import datetime

def timecheck(func):
    def wrapper(*args, **kwargs):
        # 检查时间
        if datetime.datetime.now().year == 2020:
            return func(*args, **kwargs)
    return wrapper


@timecheck
def time(name):
	print('Hello {}, 2020!'. format(name))

time("back")
```
60. 函数调用参数的传递方式是值传递还是引用传递？
视参数类型决定，
如果是可变类型：那就是传引用
如果是不可变类型，就是传值

67. 有这样一段代码，print c会输出什么，为什么？
a = 10
b = 20
c = [a]
a = 15

答：[10]

68. 交换两个变量的值？
a,b = b,a

71. Python主要的内置数据类型都有哪些？ print dir( ‘a ’) 的输出？
str, int, dict, tuple, boolean, list, set

所有带有a的内置函数

72. list(map(lambda x:x*x，[y for y in range(3)]))的输出？
[0,1,4,9]


84. 解释下什么是闭包？
简单来说就是为了在函数外部访问到函数内的局部变量的方式称为闭包

86. 生成器，迭代器的区别？


94. 请写出一段代码用正则匹配出ip？
```
In [3]: r = re.match(r'\d{3}.\d{3}.\d.\d','192.168.1.1')
```
