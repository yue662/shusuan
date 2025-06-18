t=int(input())
for i in range(t):
    n=int(input())
    sl=[]
    for j in range(n):
        ls=str(input())
        sl.append([len(ls),ls])
    sl.sort()
    k=0
    z=0
    while True:
        if z>=n-1:
            break
        d=len(sl[z][1])
        for i in range(n-z-1):
            if sl[z][1] in sl[z+i+1][1][:d]:
                k+=1
                break
        if k==1:
            break
        z+=1
    if k==0:
        print('YES')
    else:
        print('NO')