### 二叉树 

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)



104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。


# 解法 递归  深度优先搜索DFS
# 终止条件 root为None
# 每个根节点的左右节点同时遍历，每深入一层计数+1，最终返回较大的一边

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



938. 二叉搜索树的范围和
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1 深度优先搜索
# 根据二叉搜索树的特性（根节点的值永远大于它的左节点并且小于它的右节点）
# 在遍历过程中如果我们遇到根节点小于L,那么就去遍历它的右节点。如果根节点大于R,我们就去遍历它的左节点
# 通过递归的方式我们将符合条件的根节点进行累加
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        if L > root.val: return self.rangeSumBST(root.right, L, R)
        elif R < root.val: return self.rangeSumBST(root.left, L, R)

        return root.val + self.rangeSumBST(root.left, L,R) + self.rangeSumBST(root.right, L, R)


# 解法2 迭代法
# res：计数变量，对符合的数字求和  stack: 辅助栈，将可能符合条件的节点加入进栈中逐个进行检查
# 解题思路和递归一样，在遍历过程中去检查根节点的值。
# 如果在L与R的范围内，res累加
# 如果>L，则继续遍历它的左节点，可能它的左节点也符号要求
# 如果<R, 继续遍历它的右节点，直到下一个节点的值不在这三个条件中

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val > L: stack.append(node.left)
                if node.val < R: stack.append(node.right)
                if L <= node.val <= R: res += node.val
        return res



二叉树的深度            
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1 深度优先算法
# 终止条件 root为空
# 通过递归的方式从最底层开始计数计算深度，一层一层地往下找直到触发终止条件，然后从最底层一层一层返回深度值


# 解法2 BFS层序遍历
# 最直接的遍历方式，从根节点一层一层遍历下去。
# queue: 借助队列queue将当前节点的子节点存入进去作为终止条件
# tmp: 在遍历过程中借助临时列表tmp将节点存进去，每层遍历后将列表赋值给queue直到queue为空时终止
# res: 计数器
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        queue = [root]
        res = 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res+=1
        return res


# 二叉树的镜像
# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None

        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

### 贪心算法

# 1221. 分割平衡字符串

在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量

# 解法1
# 通过辅助栈进行遍历整个字符串
# 如果出现两个不相同的字符，则消掉同时检查栈是否为空，如果为空则计数器+1，否则继续遍历
# 时间复杂度：O(N)
# 空间复杂度: O(1)

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s: return 0
        stack = []
        res = 0
        for i in range(0, len(s)):
            if stack and s[i] != stack[0]:
                stack.pop()
                if not stack: res += 1
            else: stack.append(s[i])
        return res


# 解法2
# 非常简单明了的解决方式。 通过一个计数变量count来统计L与R的平衡性，如果为L则+1，如果为R则-1。直到为0时就说明检查到了平衡字符串，另外一个计数变量res则+1
# 时间复杂度O(n)
# 空间复杂度O(1)

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s: return 0
        res = 0
        count = 0
        for i in s:
            if i == 'L': count += 1
            if i == 'R': count -= 1
            if count == 0: res += 1
        
        return res



面试题32 - I. 从上到下打印二叉树

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]



# 解法 广度优先搜索
# 将根节点放入队列中，随后遍历它的子节点如果不为空则按照左右的顺序放入res列表中，随后再深入
# 终止条件： 节点为空
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res



面试题32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 广度优先搜索 队列
# 循环条件 queque不为空
# 循环过程中创建一个临时列表temp，再遍历队列，将队列中的节点值放入temp中
# 若存在子节点，左（右）子节点继续入列
# 把temp放入最终结果res中
# 时间复杂度：O(N)
# 空间复杂度: O(N)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            temp = []
            for o in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp)
        return res

