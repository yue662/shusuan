n=int(input())
sl=list(map(int,input().split()))
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
for i in range(n):
    sl[i]=TreeNode(sl[i])
for i in range(n):
    if 2*(i+1)<=n:
        sl[i].left=sl[2*(i+1)-1]
    if 2*(i+1)+1<=n:
        sl[i].right=sl[2*(i+1)]
def lj(l, r):
    l.append(r.value)
    if r.right:
        lj(l, r.right)
    if r.left:
        lj(l, r.left)
    if r.left == None and r.right == None:
        lja.append(l[:])
        print(*l)
    del l[-1]
    return
lja=[]
lj([], sl[0])
if lja[0][0]>lja[0][1]:
    check=0
    for i in lja:
        for j in range(len(i)-1):
            if i[j]<i[j+1]:
                print('Not Heap')
                check=1
                break
        if check==1:
            break
    if check==0:
        print('Max Heap')
elif lja[0][0]<lja[0][1]:
    check=0
    for i in lja:
        for j in range(len(i)-1):
            if i[j]>i[j+1]:
                print('Not Heap')
                check=1
                break
        if check==1:
            break
    if check==0:
        print('Min Heap')
else:
    print('Not Heap')