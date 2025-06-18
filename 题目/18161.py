sl=[]
for i in range(3):
    a,b=map(int,input().split())
    sl.append([])
    for j in range(a):
        sl[i].append(list(map(int,input().split())))
if len(sl[0][0])==len(sl[1]) and len(sl[0])==len(sl[2]) and len(sl[1][0])==len(sl[2][0]):
    outs=sl[2]
    for i in range(len(sl[2])):
        for j in range(len(sl[2][0])):
            for k in range(len(sl[0][0])):
                outs[i][j]+=sl[0][i][k]*sl[1][k][j]
    for i in outs:
        for j in range(len(i)-1):
            print(i[j],end=' ')
        print(i[-1])
else:
    print("Error!")