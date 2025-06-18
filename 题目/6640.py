n=int(input())
sl=[]
for i in range(n):
    sl.append(list(map(str,input().split())))
    del sl[i][0]
m=int(input())
for i in range(m):
    s=str(input())
    ch=0
    for j in range(n):
        if s in sl[j]:
            print(j+1,end=' ')
            ch=1
    if ch==0:
        print("NOT FOUND")
    print()