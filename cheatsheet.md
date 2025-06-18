# cheat sheet

1、深拷贝：得到完全独立的两变量。

浅拷贝：将对象多用一个变量记录，两变量一起改变。深拷贝仅记录值，不随之改变。

```
b=a.copy() # 浅拷贝 

import copy
c=a.deepcopy() # 深拷贝
```

2、保留小数（对num保留n位小数）

```
nums="{:.nf}".format(num)
# 或
nums="%.nf" % num
```

3、记忆化

```
from functools import lru_cache
@lru_cache
def f(x):
```

在函数前加@lru_cache，当运行到重复的自变量时自动调用之前结果。但自变量中不可含可变类型参数，如 list。

4、临时函数 lambda

格式形如：lambda arguments: expression。

arguments为一个或多个参量，expression为计算表达式，如：

```
x = lambda a : a + 10
```

可直接储存给函数名f，应用时直接f(x)。或是在其他函数之中，如：

```
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]
```

5、输出2进制：bin(x)   （x为整数int型）(结果有0b前缀)

绝对值: abs(x)

`math.ceil(number)`向上取整,`math.floor(number)` 或a//b向下取整

取模：a%b  求和 ：sum()

6、列表化:list(x)

- 字符串:`list('abc')==['a','b','c']`
- 迭代器/生成器:
  - `list(range(4))==[0,1,2,3]`
  - `list(map(int,input().split())==[2,5,1]`(假设输入'2 5 1')
  - `list(enumerate([2,5,1]))==[(0,2),(1,5),(2,1)]`（即前方赋一个位置变量）

7、集合：无重复数组

- 添加:`s.add(x)`
- 查询:`x (not) in s`,**O(1)**
- 删除:
  - `s.remove(x)`,**O(1)**
  - `s.discard(x)`,**O(1)**:删除x,如果没找到x就无事发生
- 集合运算:
  - 并:`a|b`
  - 交:`a&b`
  - 差:
    - `a-b`,注意这是表示∈a且∉b的元素的集合, 如`{1}-{1,2}==set(),{1,2}-{1}=={2}`
    - `a^b`,对称差,等于a|b-a&b
  - `a>=b,a>b,a<=b,a<b`,表示集合的包含关系,如果既不是子集也不是超集也返回False
- 构建集合:
  - 空集:`a=set()`
  - 集合化:set(x),x是列表\元组\字典(a是字典则会返回所有键组成的集合)

8、字典

- 删除:`del d[key]`
- 弹出:
  - `d.pop(key)`
- 获取:`d.get(key)`,返回键对应的值，如果key不在字典则返回None而不报错
  - `d.get(key,dft)`可以在key不在字典时返回默认值dft
- 键or值们:`d.keys()`,`d.values()`

9、欧拉筛：筛出1<=i<=n所有的素数

```
def ES(n):
  isprime=[True for _ in range(n+1)]
  prime=[]
  for i in range(2,n+1):
      if isprime[i]:
          prime.append(i)
      for j in range(len(prime)):
          if  i*prime[j]>n:break
          isprime[i*prime[j]]=False
          if i%prime[j]==0 :break
  return prime
```

求最大公约数：

```
def gcd(a, b):
  while b:
    a, b = b, a%b
  return a
```

10、ASCII码：`ord(x)` :输出对应ASCII码   `chr(x)` 输出对应字符

`s.lower()`： 将字符串全部转换为小写   `s.upper()`： 将字符串全部转换为大写

`s.capitalize()`:  将字符串化为仅有首字母大写

`s.lstrip()`： 删掉左侧空格    `s.rstrip()`： 删掉末尾空格     `s.title()`: 翻转大小写

11、index: 输出第一次检索到字符串所在位置（substring为字符串，另两个为开始与截止）

`str.index(substring, beg=0, end=len(string))`

end='' : print输出时以什么结尾，默认为换行符'\n',其余情况不会换行。

count:输出字符串中字母或子字符串个数

 `str.count(sub, start= 0,end=len(string))`

12、列表排序：

`list.sort( key=None, reverse=False)`

key为排序依据，结合临时函数 lambda运行，False为升序排列，True为降序排列

`list.reverse()`: 将列表反向

13、`global x` :定义全局变量（用于函数内）

try...except: 异常处理

```
try:
    代码
expect x:
    异常后的处理
```

x为错误类型，也可无x，对所有异常均判别。

`EOFError`：无输入，即输入为给定数量与结束标记，用于判断是否还有输入。

`KeyError`：字典里没有这个键。

14、decimal：高精度小数（y可为数字，也可用字符串导入）

```
import decimal  #导入模块
x=decimal.Decimal(y)
```

15、处理OJ的compile error 处理方法：第一行加 # pylint: skip-file 

16、堆：heapq库

```
import heapq
```

创建空堆（小顶堆）（大根堆直接对所有加负即可）：

```
heap=[]
```

将数据添加到堆中：

```
heapq.heappush(heap,num)
```

将列表化为小顶堆：

```
heapq.heapify(sl)
```

将堆顶元素出堆并将剩余元素重化为小顶堆：

```
a=heapq.heappop(heap)
```

获取最大\最小的几个元素：(n为数量，key为排序指标，配合lambda使用)

```
ml=heapq.nlagrest(n,heap,key=None)
```

```
ml=heapq.nsmallest(n,heap,key=None)
```

17、位运算的详细特性和示例：

   1.与运算（AND）：

- 任何数和0做与运算，结果是0，即 x & 0 = 0。例如，5（101） & 0 = 0。
- 任何数和其自身做与运算，结果是自身，即 x & x = x。例如，5（101） & 5（101） = 5（101）。

   2.或运算（OR）：

- 任何数和0做或运算，结果是自身，即 x | 0 = x。例如，5（101） | 0 = 5（101）。

- 任何数和其自身做或运算，结果是自身，即 x | x = x。例如，5（101） | 5（101） = 5（101）。

   3.异或运算（XOR）：

- 任何数和0做异或运算，结果是自身，即 x ^ 0 = x。例如，5（101） ^ 0 = 5（101）。
- 任何数和其自身做异或运算，结果是0，即 x ^ x = 0。例如，5（101） ^ 5（101） = 0。
- 异或运算满足交换律和结合律，即 a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c。例如，5（101） ^ 3（011） ^ 4（100） = 5 ^ (3 ^ 4) = (5 ^ 3) ^ 4。

   4.非运算（NOT）：

- 非运算会反转操作数的所有位。例如，~5（101） = 2（010）。

   5.左移运算（SHL）：

- 左移n位等于乘以2的n次方，即 x << n = x * 2^n。例如，5（101） << 2 = 20（10100）。
- 左移运算不改变操作数的符号位。

   6.逻辑右移运算（SHR）：

- 右移n位等于除以2的n次方，即 x >> n = x / 2^n。例如，20（10100） >> 2 = 5（101）。
- 逻辑右移运算会用0填充移位后产生的空位。

   7.算术右移运算（SAR）：

- 算术右移运算会用符号位填充移位后产生的空位，因此它可以保持负数的符号。例如，对于负数-5（1011） >>> 2 = -2（1110）。

18、字典树：存储，查找字符串

对每个字母进行存储，形成树的结构。

```
class TrieNode:
    def __init__(self):
        self.child={}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, nums):
        curnode = self.root
        for x in nums:
            if x not in curnode.child:
                curnode.child[x] = TrieNode()
            curnode=curnode.child[x]
    def search(self, num):
        curnode = self.root
        for x in num:
            if x not in curnode.child:
                return 0
            curnode = curnode.child[x]
        return 1
```

两函数分别为输入与查找，若查找的字符串为树中字符串前缀或相同，则输出1，否则为0

19、邻接表

图的一种表现形式，将每个顶点的邻居顶点存储为列表，即为邻接表。

 graph = { 'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C'] }

20、Dijkstra算法：有权无向图的最短路径算法

由初始顶点开始，记录相邻顶点与其距离，之后选取距离最小顶点，更新与其相邻顶点距初始顶点距离，使距离最小，再选取距离最小顶点重复过程。（仅边权为正）

记录路径：记录到达每一个节点的前一节点，相当于链表操作，之后递推即可。

含最终条件的Dijkstra算法（如总参数和小于某值）：

在每次找到最短后不将其弹出，而是记录此时情况，令其距离继续变化，不断找到想要的节点，直到符合条件为止。本质上，此即为按照路径长度进行广搜的操作。

21、并查集

（1） 初始化
并查集通过一个数组 parent 来表示每个元素的父节点，另一个数组 rank 用于优化合并操作。以下是初始化的代码：

```
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
```

（2）查找操作与路径压缩
查找操作用于找到某个元素所在集合的根节点。路径压缩技术通过将访问过的节点直接连接到根节点上，从而降低树的高度，提高后续查找操作的效率。以下是路径压缩的实现代码：

```
def find(self, p):
    if self.parent[p] != p:
        self.parent[p] = self.find(self.parent[p])  # 路径压缩
    return self.parent[p]
```

（3）合并操作与按秩合并
合并操作用于将两个不相交的集合合并为一个集合。按秩合并技术确保在合并操作中总是将高度较小的树连接到高度较大的树上，从而避免增加树的高度。以下是按秩合并的实现代码：

```
def union(self, p, q):
    rootP = self.find(p)
    rootQ = self.find(q)
    if rootP != rootQ:
        if self.rank[rootP] < self.rank[rootQ]:
            rootP, rootQ = rootQ, rootP  # 确保rootP是秩较高的树根
        self.parent[rootQ] = rootP
        if self.rank[rootP] == self.rank[rootQ]:
            self.rank[rootP] += 1  # 更新秩
```

并查集的应用

（1）判断连通性
并查集可以用于判断两个节点是否连通。通过检查它们的根节点是否相同即可判断。

```
def connected(self, p, q):
    return self.find(p) == self.find(q)
```

（2）计算连通分量
并查集还可以用于计算连通分量的数量。在初始状态下，每个节点都是一个独立的连通分量，随着合并操作的进行，连通分量的数量逐渐减少。（即判断存在多少独立的树）

```
def count_components(self):
    root_set = set()
    for i in range(len(self.parent)):
        root_set.add(self.find(i))
    return len(root_set)
```

22、最小生成树

当图中每条边都存在权重时,我们从图中生成一棵树(n - 1 )条边时,生成这棵树的总代价就是每条边的权重相加之和。最小生成树，就是在边中选择N-1条出来，连接所有的N个点。这N-1条边的边权之和是所有方案中最小的。

Prim算法每次循环都将一个蓝点u变为白点，并且此蓝点u与白点相连的最小边权min[u]还是当前所有蓝点中最小的。这样相当于向生成树中添加了n-1次最小的边，最后得到的一定是最小生成树。(V为顶点列表，E为邻接矩阵)（适合稠密图）

```
import math
# 定义生成Y集合的方法
def create_Y(X):
    Y = []
    for point in V:
        if point not in X:
            Y.append(point)
    return Y
# 编写Prim算法
def Prim(V, E):
    # 1.定义变量
    weight = math.inf
    point1 = 0
    point2 = 0
    # 2.编写Prim算法
    for i in range(len(V)):
        if V[i] in X:  # 确定了顶点集合X中元素在顶点集合V中的下标，间接的确定了在边集合中的一个下标
            for j in range(len(V)):
                if V[j] in create_Y(X):  # 确定了顶点集合Y中元素在集合V中的下标，间接确定了在边集合中的另一个下标
                    if (E[i][j] != None) and (E[i][j] < weight):  # 循环判断，找到顶点集合X到Y之间最小权值的边
                        weight = E[i][j]
                        point1 = V[i]
                        point2 = V[j]
    print(weight, point1 , point2)  # 将生成树的这条边进行显示
    X.append(point2)  # 将该点加入到操作集合X中
X = [V[0]]
count = 0
while True:
    if count < len(V) - 1:
        Prim(V, E)
        count = count + 1
    else:
        break
```

Kruskal算法将一个连通块当做一个集合。Kruskal首先将所有的边按从小到大顺序排序（一般使用快排），并认为每一个点都是孤立的，分属于n个独立的集合。然后按顺序枚举每一条边。如果这条边连接着两个不同的集合，那么就把这条边加入最小生成树，这两个不同的集合就合并成了一个集合；如果这条边连接的两个点属于同一集合，就跳过。直到选取了n-1条边为止。

```
class DisjointSet:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
def kruskal(graph):
    num_vertices = len(graph)
    edges = []
    # 构建边集
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    # 按照权重排序
    edges.sort(key=lambda x: x[2])
    # 初始化并查集
    disjoint_set = DisjointSet(num_vertices)
    # 构建最⼩⽣成树的边集
    minimum_spanning_tree = []
    for edge in edges:
        u, v, weight = edge
    if disjoint_set.find(u) != disjoint_set.find(v):
        disjoint_set.union(u, v)
    minimum_spanning_tree.append((u, v, weight))
    return minimum_spanning_tree
```

23、括号内为分隔符，将字符串分割为列表。

```
str.split(str="")
```

24、链表：每个节点只有⼀个指针，指向下⼀个节点。链表的头部指针指向第⼀个节点，⽽最后⼀个节点 的指针为空（指向  None ）。

```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
```

三个函数分别为尾部插入，删除（任意值），输出链表。

双向链表：主要用于浏览器记录等以及双端队列。

```
class Node:
 	def __init__(self, data):
 		self.data = data  # 节点数据
		self.next = None  # 指向下⼀个节点
		self.prev = None  # 指向前⼀个节点
class DoublyLinkedList:
 	def __init__(self):
 		self.head = None  # 链表头部
		self.tail = None  # 链表尾部
	# 在链表尾部添加节点
	def append(self, data):
 		new_node = Node(data)
 		if not self.head:  # 如果链表为空
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    # 在链表头部添加节点
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # 如果链表为空
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    # 删除链表中的指定节点
    def delete(self, node):
        if not self.head:  # 链表为空
            return
        if node == self.head:  # 删除头部节点
            self.head = node.next
            if self.head:  # 如果链表⾮空
                self.head.prev = None
        elif node == self.tail:  # 删除尾部节点
            self.tail = node.prev
            if self.tail:  # 如果链表⾮空
                self.tail.next = None
        else:  # 删除中间节点
            node.prev.next = node.next
            node.next.prev = node.prev
        node = None  # 删除节点
    # 打印链表中的所有元素，从头到尾
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    # 打印链表中的所有元素，从尾到头
    def print_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
```

25、单链表反转算法：输出反转后的头节点。

```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next  # 暂存当前节点的下⼀个节点
        curr.next = prev  # 将当前节点的下⼀个节点指向前⼀个节点
        prev = curr  # 前⼀个节点变为当前节点
        curr = next_node  # 当前节点变更为原先的下⼀个节点
    return prev
```

26、前中后缀表示法：前缀与后缀表示法无需用括号确定运算顺序，操作符相对于它们所操作的操作数不再有歧义。

转换：将中序表达式完全括号化，即所有操作两端均加上括号，之后把运算符移至左（右括号处），并删去对应右（左）括号，即转换为前（后）序表达式。

中缀转后缀：（输入时将所有数与运算符，括号间用空格分割）

```
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in '*/+-':
            while opStack and (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)
        else:
            postfixList.append(token)
    while opStack:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
```

后缀表达式求值：

```
def postfixEval(postfixExpr):
    operandStack = []
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.append(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.append(result)
    return operandStack.pop()
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
```

27、树的遍历：

前序遍历（Preorder）：根 -> 左⼦树 -> 右⼦树 （先根遍历，适用多叉树，先遍历根节点再访问子树）

中序遍历（Inorder）：左⼦树 -> 根 -> 右⼦树 

后序遍历（Postorder）：左⼦树 -> 右⼦树 -> 根（后根遍历，适用多叉树，先遍历子树再访问根节点）

```
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

```
 # 前序遍历
def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)
 # 中序遍历
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)
 # 后序遍历
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")
```

⼆叉搜索树（Binary Search Tree，BST）：对于任意节点，左⼦树的所有节点值⼩于该节点值， 右⼦树的所有节点值⼤于该节点值。

对二叉搜索树，其中序遍历可实现快速排序，排序结果即为升序排列。

```
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(node, value):     #插入函数，node为根节点
    if node is None:
        return TreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    return node
```

平衡⼆叉树：左右两个⼦树的⾼度差不超过1，且它的左子树和右子树都是一颗平衡二叉树。

 AVL树：平衡⼆叉搜索树

扩充二叉树：在二叉树出现空子树的位置增加空树叶所形成的二叉树，即所有叶子节点后加入两空子节点。最终所有叶子节点为空节点且为满二叉树。

霍夫曼编码：构造一棵 扩充二叉树，使得所有 叶子节点的带权路径长度和最小。

思路：我们通过以下贪心策略构造一棵最优二叉树：

1. 将所有权值作为初始节点，放入一个最小堆中。
2. 重复执行以下操作直到只剩一个节点：
   - 从堆中取出两个最小权值节点 `a` 和 `b`
   - 合并为一个新节点，权值为 `a + b`
   - 把这个新节点的权值加入堆
   - 这次合并会产生一个代价：`a + b`，将其加入总路径代价中
3. 最终累加的合并代价即为 最小外部带权路径长度总和。

 嵌套括号表示法 ：对根节点，将子节点放入其后括号中，每个子节点同样操作。

邻接表表示法：将每个节点列出，其子节点放入其后列表。

28、哈夫曼编码树

霍夫曼编码算法从字符串X中每个独特的d个字符开始，每个字符都是单节点⼆叉树的根节点。算法以⼀系列的 轮次进⾏。在每⼀轮中，算法将具有最⼩频率的两棵⼆叉树合并为⼀棵⼆叉树。此过程复进⾏，直到只剩下 ⼀棵树为⽌。

最终二叉树T中的每条边代表码字中的⼀ 位，到左孩⼦的边代表“0”，到右孩⼦的边代表“1”。到字符的边权相连即为其霍夫曼编码。

29、二叉堆

完全⼆叉树：除了最底层，其他每⼀层的节点都是满的。可以⽤⼀个列表来表示它。、

对于在列表中处于位置 p 的节点来说，它的左⼦节点正好处于位置 2p；同理，右 ⼦节点处于位置 2p+1。给定列表中位置  n 处的节点，其⽗节点的位置就是 n//2。

```
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    def insert(self, k):       #向⼆叉堆中新加元素
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    def delMin(self):      #删除最小元素
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def buildHeap(self, alist):     #根据元素列表构建堆
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            print(f'i = {i}, {self.heapList}')
            self.percDown(i)
            i = i - 1
        print(f'i = {i}, {self.heapList}')
```

30、拓扑排序：使得对于任意的有向边 (u, v)，顶点 u 在排序中出现在顶点 v 的前⾯。

Kahn算法：将所有入度为0的顶点逐渐弹出，之后令其邻居入度减1，重复这一过程。只要是有向⽆环图（DAG），总能实现到全部弹出。

31、散列表：散列查找法：元素的存储和其关键字之间建⽴某种直接关系

（1）、平⽅取中法：取关键字平⽅后的中间⼏位或其组合作为散列地址，随机分布的关键字 得到的散列地址也是随机的。

（2）、折叠法：关键字分割成位数相同的⼏部分（最后⼀部分的位数可以不同），然后取这⼏部分的叠加和（舍去进位）作为 散列地址。

（3）、 除留余数法：假设散列表表⻓为 m，选择⼀个不⼤于m 的数p，⽤p去除关键字，除后所得余数为散列地址，即 H(key) = key%p，一般选p为⼩于表⻓的最⼤质数。

处理冲突方法：![image-20250526152126530](C:\Users\yue\AppData\Roaming\Typora\typora-user-images\image-20250526152126530.png)

(1) 线性探测法 ：di = 1, 2, 3, …, m-1 ，将散列表假想成⼀个循环表，超出则回到初始。

(2)⼆次探测法： ![image-20250526152323853](C:\Users\yue\AppData\Roaming\Typora\typora-user-images\image-20250526152323853.png)

(3)伪随机探测法 ：di = 伪随机数序列

(4)链地址法:把具有相同散列地址的记录放在同⼀个单链表中，称为同义词链表。

32、二分查找模版：

```
def binary_search:
    def check(n):
        if ....:
            return True
        else:
            return False
    st=1
    ed=max(nums)+1
    outs=0
    while st<ed:
        mid=(st+ed)//2
        if check(mid):
            ed=mid
            outs=mid
        else:
            st=mid+1
    return outs
```

33、相交链表：寻找两链表开始相交节点

    def xj(headA,headB):
        if not headA or not headB:
                return None
        pointerA, pointerB = headA, headB
        while pointerA is not pointerB:
            # 如果到达链表末尾，则转向另一个链表的头部
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
        # 两种情况下会退出循环：
        # 1. 在交点相遇
        # 2. 两个链表都遍历完没有交点（此时 pointerA 和 pointerB 都为 None）
        return pointerA

34、判断回文：s[::-1] 为列表反转。

```
def is_palindrome(s):
    return s == s[::-1]
```
