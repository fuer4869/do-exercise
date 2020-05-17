---
title: leetcode刷题笔记（二）
date: 2019-10-23 18:50:29
tags: 算法, leetcode
category: 笔记
---
### 旋转数组

***给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]***

#### 解法1 拼接法
**解题思路**
第一步求出了k与nums长度的余数是为了避免出现```k>len(nums)```的情况出现
然后在进行切片，把切下来的倒数k个元素放到列表最前面即可
值得注意的是，在python中以```nums = nums[-k:]+....```的形式不能顺利赋值，
需要以全切的方式```nums[:]```才可以。这个细节不是很清楚

`
	class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
	if k == 0: return
	k = k%len(nums)
	nums[:] = nums[-k:] + nums[:-k]
`

#### 解法2 三次翻转
**解题思路**
步骤如下：
根据k，可以把数组拆分成两段，把这两段进行分别翻转。如k=3
[1,2,3,4,| 5,6,7]
我把数组拆分成了[1,2,3,4]和[5,6,7]
翻转第一步：[7,6,5,4,3,2,1]
翻转第二步:  [5,6,7,4,3,2,1]
翻转第三步：[5,6,7,1,2,3,4]

```  
if k==0:return

        k%=len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
```

#### 解法3  环状替换
**解题思路**
遍历整个列表，将每个元素往后移动k个位置，将被替换的元素临时存储在temp中，继续往后替换。
时间复杂度：执行次数为数组的长度O(n)
空间复杂度：使用了常数个额外空间O(1)

```
        if k==0:return
        size = len(nums)
        k%=size
        count=0 #计数
        start=0
        while count < size:
            target=start
            temp = nums[start]
            while True:
                target = (target+k)%size
                temp,nums[target] = nums[target],temp
                count += 1
                if count >= size or target == start:
                    break
            start += 1
```
