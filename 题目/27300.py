n=int(input())
sl={}
sl0=[]
for i in range(n):
    k=str(input())
    z=k.index('-')
    if k[:z] in sl:
        sl0[sl[k[:z]]].append((k[z+1:]))
    else:
        sl[k[:z]]=len(sl)
        sl0.append([k[z+1:]])
for m in range(len(sl)):
    for p in range(len(sl0[m])):
        if 'B' in sl0[m][p][-1]:
            sl0[m][p]=(float(sl0[m][p][:-1])*1000,sl0[m][p])
        else:
            sl0[m][p]=(float(sl0[m][p][:-1]),sl0[m][p])
    sl0[m].sort()
for j in sorted(sl):
    lj=''
    for k in sl0[sl[j]]:
        lj+=' '+str(k[1])+','
    print(str(j)+':'+lj[:-1])