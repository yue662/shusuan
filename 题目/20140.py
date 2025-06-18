def check(n,st):
    if '[' in st:
        k1=st.index('[')
        o=1
        if ord(st[k1+2])<=57:
            o=2
        if len(st)>=6:
            if ord(st[k1+3])<=57:
                o=3
        s1=0
        s2=0
        for i in range(1, len(st)):
            if st[k1+i] in ['[']:
                s1+=1
            if st[k1+i] in [']']:
                if s1==s2:
                    k2=k1+i
                    break
                else:
                    s2+=1
        if k2==len(st)-1:
            return (st[:k1]+check(int(st[k1+1:k1+o+1]),st[k1+o+1:-1]))*n
        else:
            return (st[:k1]+check(int(st[k1+1:k1+o+1]),st[k1+o+1:k2])+check(1,st[k2+1:]))*n
    else:
        return st*n
s=str(input())
print(check(1,s))