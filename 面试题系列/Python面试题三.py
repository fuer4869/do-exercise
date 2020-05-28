# import os

# s_path = 'django-practice'
# def print_directory_contents(path):
#     for s_cild in os.listdir(path):
# 	    s_child_path = os.path.join(path, s_cild)
# 	    if os.path.isdir(s_child_path):
# 		    print_directory_contents(s_child_path)
# 	    else:
# 		    print(s_child_path)
	


# print_directory_contents(s_path)


### 单例
# def singleton(cls):
# 	instances={}
# 	def wrapper(*args, **kwargs):
# 		if cls not in instances:
# 			instances[cls] = cls(*args, **kwargs)
# 		return instances[cls]
# 	return wrapper


# class Singleton(object):
	# def __new__(cls, *args, **kwargs):
		# if not hasattr(cls, '_instance'):
			# cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		# return cls._instance

# @singleton
# class Foo(Singleton):
	# pass
# foo1 = Foo()
# foo2 = Foo()
# print(foo1 is foo2)


"""18.反转一个整数，例如-123 --> -321"""
class Solution(object):
	"""docstring for Solution"""
	def reverse(self, x):
		if -10<x<10:
			return x
		strs = str(x)
		if strs[0] != "-":
			strs = strs[::-1]
			x = int(strs)
		else:
			strs = strs[1:][::-1]
			x = int(strs)
			x=-x
		return x


s = Solution()
print(s.reverse(321))


"""
19.设计实现遍历目录与子目录，抓取.pyc文件

"""
import os

def get_files(dir, suffix):
	res = []
	for root,dirs,files in os.walk(dir):
		for filename in files:
			name,suf = os.path.splitext(filename)
			if suf == suffix:
				res.append(os.path.join(root, filename))

	print(res)


get_files('./', '.py')


"""
21.Python-遍历列表时删除元素的正确做法
"""

a = [1,2,3,4,5,6,7,8]
print(id(a))
# print(id(a[:]))
# for i in a[:]:
#     if i>5:
#         pass
#     else:
#         a.remove(i)
#     print(a)
# print('-----------')
# print(id(a))

# b = filter(lambda x:x>5, a)
# print(list(b))


for i in range(len(a)-1, 0, -1):
	if a[i]>5:
		pass
	else:
		a.remove(i)
print(id(a))
print('---------')
print(a)


"""
全字母短句 PANGRAM 是包含所有英文字母的句子，
比如：A QUICK BROWN FOX JUMPS OVER THE LAZY DOG. 
定义并实现一个方法 get_missing_letter, 传入一个字符串采纳数，
返回参数字符串变成一个 PANGRAM 中所缺失的字符。应该忽略传入字符串参数中的大小写，
返回应该都是小写字符并按字母顺序排序（请忽略所有非 ACSII 字符）

"""
def get_missing_letter(a):
	s1 = set("abcdefghijklmnopqrstuvwxyz")
	s2 = set(a.lower())

	ret = "".join(sorted(s1 - s2))
	return ret


# print(get_missing_letter("python"))

23. 可变类型和不可变类型

可变类型：
list, dict
不可变类型：
str, int, tuple

当进行修改操作时，可变类型不会重新分配内存，而不可变类型则会重新开辟新的内存


24.is和==有什么区别？

is比较的是双方的内存地址
==比较的是双方的值是否相等
===则是两者


# 25.求出列表所有奇数并构造新列表

a = [1,2,3,4,5,6,7,8,9,10]

b = [i for i in a if i%2==1]
print(b)

# 26. 用一行python代码写出1+2+3+10248
print(sum([1,2,3,10248]))


# 27.Python中变量的作用域？（变量查找顺序)
# 函数作用域
# LEGB
# 1. local
# 2. enclosing
# 3. global
# 4. build-in

m = 10
def fun5():
    # m = 100 
    def fun6():
        print(m)
        print('fun6')
    return fun6           # 反映 函数的引用 
fun5()()


# 28.字符串 "123" 转换成 123，不使用内置api，例如 int()

a = "123"
num = 0
for i in a:
	num = num * 10 + ord(i) - ord('0')

# print(num)

"""
29. 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
"""

def find_sum(nums, target):
	res = []
	start = 0
	while start < len(nums):
		if target - nums[start] in nums:
			return [nums.index(nums[start]), nums.index(target - nums[start])]
		else:
			start = start + 1

# print(find_sum([2,7,7,11,15],9))


"""
31.统计一个文本中单词频次最高的10个单词？

"""
import re

def statist_word(filepath):
    res = {}
    with open(filepath) as f:
        for line in f:
            line = re.sub("\W+", " ",line)
            lineone = line.split()
            for keyone in lineone:
                if keyone in res:
                    res[keyone] += 1
                else:
                    res[keyone] = 1
    
    result = sorted(res.items(), key=lambda x:x[1], reverse=True)[:10]
    result = [x[0] for x in result]
    print(result)

# statist_word('test.txt')


"""
32.请写出一个函数满足以下条件
该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：

1、该元素是偶数

2、该元素在原list中是在偶数的位置(index是偶数)

"""

def get_even(nums):
	return [i for i in nums if i%2==0 and nums.index(i)%2==0]

# print(get_even([0,1,2,3,4,5,6,7,8,9,10]))


"""
33.使用单一的列表生成式来产生一个新的列表
该列表只包含满足以下条件的值，元素为原始列表中偶数切片

"""
data = [1,2,5,8,10,3,18,6,20]
result = [i for i in data[::2]]
# print(result)


"""
34.用一行代码生成[1,4,9,16,25,36,49,64,81,100]

"""
res = list(map(lambda x:x**2, range(1,11)))

res2 = [x**2 for x in range(1,11)]
# print(res2)


"""
37.给定一个任意长度数组，实现一个函数
让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'

""" 
def sort_oddeven(nums):
    odd = []
    even = []
    for i in nums:
        if i%2 == 1:
            odd.append(i)
        else:
            even.append(i)
    odd = sorted(odd, reverse=False)
    even = sorted(even, reverse=True)
    return odd+even
# print(sort_oddeven([1,9,8,2,3,7,6,4,5,5]))

"""
37.给定一个任意长度字符串，实现一个函数
让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'

"""
def sort_str(strs):
    if len(strs) < 2:
        return strs
    l = [int(i) for i in strs]
    l.sort(reverse=True)
    for i in range(0, len(l)):
        if l[i] % 2 == 1:
            l.insert(0, l.pop(i))
    return "".join([str(b) for b in l])
# print(sort_str('1982376455'))


"""
39.阅读一下代码他们的输出结果是什么？
"""
def multi():
    return [lambda x : i*x for i in range(4)]

# print([m(3) for m in multi()])
# [9,9,9,9]

"""
40.统计一段字符串中字符出现的次数
"""
def count_str(strs):
	sdic = {}
	for i in strs:
		sdic[i] = sdic.get(i, 0)+1
	return sdic

str_dic = count_str("AABBCCAAD")





	
