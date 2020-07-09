1266. 访问所有点的最小时间
平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。

你可以按照下面的规则在平面上移动：

每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
必须按照数组中出现的顺序来访问这些点。
 

示例 1：



输入：points = [[1,1],[3,4],[-1,0]]
输出：7
解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
从 [1,1] 到 [3,4] 需要 3 秒 
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒

# 题解 
# 很简单的思路 利用切比雪夫距离
# 切比雪夫距离 ：
# 二个点之间的距离定义是其各坐标数值差绝对值的最大值
# 那结合到题目中就是通过两点|x1-x2| 与 |y1-y2|中的最大值就是我们要求的距离

# 时间复杂度O(N)
# 空间复杂度O(1)

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(1, len(points)):
            x0 = abs(points[i][0] - points[i-1][0])
            y0 = abs(points[i][1] - points[i-1][1])
            steps += max(x0, y0)
        return steps



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


1480. 一维数组的动态和
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。
# 简单的动态和解法
# result[i] + nums[i+1]
# 时间复杂度: O(n)
# 空间复杂度: O(1)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = nums
        for i in range(1, len(nums)):
            result[i] = result[i-1] + result[i]
        return result


1470. 重新排列数组
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

 
示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

# 把n这个中位数与循环中的i联系起来
# 时间复杂度O(n)
# 空间复杂度O(1)

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) <= 2: return nums
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result


16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

# 解法 双指针
# 题目的意思其实就是列表中三个值的和与目标target之差的绝对值，找到最小的那组
# 为了避免重复捕获，先对列表进行排序, 拿到初始三个数之和ans: nums[0] + nums[1] + nums[2] 
# 然后遍历列表，以i为初始捕获对象，nums[i+1]和nums[n-1]作为参考值
# 对该三个数字的和 sums 与target不断进行比较，设s = abs(target - sums)
# 调整逻辑：如果s < abs(target-ans)，说明sums相比ans更接近target，将sums赋值给ans
# 如果sums大于target，说明我们可以往小调试试看能不能找到更接近target的组合: e-=1,反之则s+=1
# 如果没有更接近的组合了就返回ans

# 时间复杂度： O(n^2)
# 空间复杂度: O(n)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]

        for i in range(n):
            s,e = i+1, n-1
            while s < e:
                sums = nums[i] + nums[s] + nums[e]
                if abs(target - sums) < abs(target - ans):
                    ans = sums
                if sums > target: e -= 1
                elif sums < target: s += 1
                else: return ans
        return ans


1431. 拥有最多糖果的孩子
给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。

 

示例 1：

输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true] 
解释：
孩子 1 有 2 个糖果，如果他得到所有额外的糖果（3个），那么他总共有 5 个糖果，他将成为拥有最多糖果的孩子。
孩子 2 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
孩子 3 有 5 个糖果，他已经是拥有最多糖果的孩子。
孩子 4 有 1 个糖果，即使他得到所有额外的糖果，他也只有 4 个糖果，无法成为拥有糖果最多的孩子。
孩子 5 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。


# 计算出列表中最大值
# 遍历列表对其中每个元素与最大值进行比较返回boolean
# 时间复杂度O(n)
# 空间复杂度O(1)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        top = max(candies)
        for i in candies:
            result.append((i + extraCandies) >= top)

        return result




349. 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]



# 解法1 内置函数 set集合去重
# &交集
# 时间复杂度 O(m+n)
# 空间复杂度 O(m+n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
         if not nums1 or not nums2: return []
         s1 = set(nums1)
         s2 = set(nums2)
         return list(s1 & s2)


#解法2
# 二分查找（不是最优解）
# 通过遍历长度比较短的list作为目标对另外一个list进行二分查找
# 时间复杂度：O(nlogn)
# 空间复杂度：O(nlogn)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []
        if len(nums1) < len(nums2): 
            for i in nums1:
                if(self.binarySearch(nums2, i) is not None): res.append(i)
        else: 
            for i in nums2:
                if(self.binarySearch(nums1, i) is not None): res.append(i)
        return set(res)

    
    def binarySearch(self, nums, target):
        start = 0
        high = len(nums) -1
        while start <= high:
            mid = (start + high)//2
            guess = nums[mid]
            if guess == target: return guess
            if guess < target: start = mid + 1
            else: high = mid -1
        return None


