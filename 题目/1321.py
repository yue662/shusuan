# pylint: skip-file
def num(k,min,zl,check):
    global nu
    if k==0:
        nu+=1
        return
    kl=[]
    for p in range(a):
        for q in range(a):
            kl.append(zl[p][q])
    if 1 not in kl:
        return
    for h in range(min,a):
        for z in range(a):
            if zl[h][z]==1 and check[z]==0:
                k-=1
                check[z]=1
                num(k,h+1,zl,check)
                k+=1
                check[z]=0
while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    sl=[]
    nl=[]
    for i in range(a):
        sl.append(str(input()))
        nl.append([0]*a)
        for j in range(a):
            if '#' in sl[i][j]:
                nl[i][j]=1
    nu=0
    check=[0]*a
    num(b,0,nl,check)
    print(nu)