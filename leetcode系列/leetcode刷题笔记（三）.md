---
title: leetcode刷题笔记（三）
date: 2019-10-24 13:22:19
tags: 算法, leetcode
category: 笔记
---
### 题目1 对有序数组删除重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。


### 解答
**解题思路**
因为nums是一个排序数组，所以重复项只会出现在相邻的位置。可以通过双指针的方式来指定其中的元素，
然后逐步往后移动进行比对，直到找到相邻且相等的元素删除即可。有一点要注意的是，如果连续出现三个
重复的元素，用两两比对会漏掉一个，这个时候需以第一个重复元素为参照物进行比对，直到删除了所有的
重复项后再往后移动。

**实现代码：**
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                left += 1
                right += 1
        return len(nums)
```


### 题目2  合并两个有序数组

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]


#### 解答
解法1：合并后排序
十分直接的算法。利用切片可以很方便的进行合并
没有产生额外的使用空间，由于最后对数组进行了排序处理，所以时间复杂度较高
时间复杂度：O((n+m)log(n+m))
空间复杂度：O(1)
```
nums1[:] = sorted(nums1[:m] + nums2[:n])
```

解法2：双指针
解题思路：
 双指针
        因为两个数组都是有序数组，一下子就能想到可以通过双指针x,y分别指向nums1和nums2
        然后通过循环将最小的值进行比对放入nums1中。
        因为最终结果必须呈现在nums1中，所以nums1原来的值就暂时放在额外的数组中作为循环中使用
        还有收尾工作，如果出现一个中的比对完了，另外个数组还有剩余的情况，就把剩下的放入nums1中。

        空间上由于额外创建了个等于nums1的数组，所以
        空间复杂度：O(m)
        时间复杂度：O(m+n)

	代码：
	```
	class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        x = 0
        y = 0
        nums1_copy = nums1[:m]
        nums1[:] = []
        while y < n and x < m:
            if nums1_copy[x] < nums2[y]:
                nums1.append(nums1_copy[x])
                x += 1
            else:
                nums1.append(nums2[y])
                y += 1
        if x < m:
            nums1[:] += nums1_copy[x:]
        if y < n:
            nums1[:] += nums2[y:]
	```
