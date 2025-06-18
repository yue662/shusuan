import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
outl=[0]*m
outs=[0]*n
for i in range(n):
    p=num_list[i]%m
    p1=p
    k=1
    o=0
    while True:
        if outl[p1]==0 or outl[p1]==num_list[i]:
            outl[p1]=num_list[i]
            outs[i]=p1
            break
        else:
            p1=(p+(k**2)*((-1)**o))%m
            o+=1
            if o==2:
                k+=1
                o=0
print(*outs)