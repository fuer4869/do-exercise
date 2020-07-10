LCP 01. 猜数字
小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？

 

输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。

 

示例 1：

输入：guess = [1,2,3], answer = [1,2,3]
输出：3
解释：小A 每次都猜对了。

# 题解
# 很简单的题目
# 直接对每个元素进行比较，对比较后的值进行累加即可
# 时间复杂度O(N)
# 空间复杂度O(1)

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return ((guess[0] == answer[0]) + (guess[1] == answer[1]) + (guess[2] == answer[2]))
