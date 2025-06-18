n=int(input())
sl=list(map(int,input().split()))
outs=[]
for i in range(len(sl)):
    for j in range(i+1,len(sl)):
        outs.append([abs(sl[i]+sl[j]-n),sl[i]+sl[j]])
outs.sort()
out=[]
for i in range(len(outs)):
    if outs[i][0]==outs[0][0]:
        out.append(outs[i][1])
    else:
        break
print(min(out))