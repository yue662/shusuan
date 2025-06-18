while True:
    try:
        n=int(input())
        sl=[]
        for i in range(n):
            sl.append(list(map(int,input().split())))
        inl=[0]
        outl=list(range(1,n))
        all=0
        while True:
            k=sl[inl[0]][outl[0]]
            o=outl[0]
            for i in inl:
                for j in outl:
                    if sl[i][j]<k:
                        o=j
                        k=sl[i][j]
            inl.append(o)
            outl.remove(o)
            all+=k
            if len(outl)==0:
                break
        print(all)
    except EOFError:
        break