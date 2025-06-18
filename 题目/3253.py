while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    sl=[]
    outs=[]
    b-=1
    for i in range(a):
        sl.append(i+1)
    for j in range(a):
        b=(c+b-1)%a
        outs.append(sl.pop(b))
        a-=1
    print(','.join(map(str,outs)))