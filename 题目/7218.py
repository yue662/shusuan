t=int(input())
jl=[[1,0],[0,1],[-1,0],[0,-1]]
for i in range(t):
    r,c=map(int,input().split())
    sl=[]
    check=[]
    for _ in range(r):
        o=str(input())
        sl.append([u for u in o])
        check.append([0]*c)
    z1=[]
    z2=[]
    for j in range(r):
        for k in range(c):
            if sl[j][k]=='S':
                z1=[j,k]
                check[j][k]=1
            elif sl[j][k]=='E':
                z2=[j,k]
    zl=[[z1]]
    e=0
    while True:
        zl.append([])
        for j in zl[-2]:
            for z in range(4):
                x,y=j[0]+jl[z][0],j[1]+jl[z][1]
                if 0<=x<r and 0<=y<c and check[x][y]==0:
                    if sl[x][y]=='.':
                        zl[-1].append([x,y])
                    elif x==z2[0] and y==z2[1]:
                        print(len(zl)-1)
                        e=1
                        break
                    check[x][y]=1
            if e==1:
                break
        if e==1:
            break
        if len(zl[-1])==0:
            break
    if e==0:
        print('oop!')
