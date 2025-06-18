n=int(input())
sl=[]
k=0
for _ in range(2*n):
    st=str(input())
    if 'a' in st:
        sl.append(int(st[4:]))
    else:
        if sl[-1]==min(sl):
            del sl[-1]
        else:
            sl.sort(reverse=True)
            del sl[-1]
            k+=1
print(k)