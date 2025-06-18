n=int(input())
sl=list(map(str,input().split()))
ln=[[],[],[],[],[],[],[],[],[]]
lz=[[],[],[],[]]
dic={'A':0,'B':1,'C':2,'D':3,0:'A',1:'B',2:'C',3:'D'}
for i in range(n):
    num=int(sl[i][1])
    ln[num-1].append(sl[i])
    zm=dic[sl[i][0]]
    lz[zm].append(sl[i])
for i in range(4):
    lz[i].sort()
for i in range(9):
    print('Queue'+str(i+1)+':',end='')
    print(*ln[i])
for i in range(4):
    print('Queue'+dic[i]+':',end='')
    print(*lz[i])
for i in range(4):
    print(*lz[i],end=' ')