n=int(input())
jo=0
list=[]
zw=[]
len=0
for i in range(n):
    a=str(input())
    if 'a' in a:
        list.append(int(a[4:]))
        jo+=1
        jo%=2
        len+=1
        if jo==0:
            zw.append(list[int(len/2)])
        else:
            if len==1:
                zw.append(list[0])
            else:
                del zw[0]
    elif 'd' in a:
        del list[0]
        jo+=1
        jo%=2
        len-=1
        if jo==0:
            if len==0:
                zw=[]
            else:
                zw.append(list[int(len/2)])
        else:
            del zw[0]
    else:
        out=sum(zw)/(2-jo)
        if out%1==0:
            print(int(out))
        else:
            print(float(out))