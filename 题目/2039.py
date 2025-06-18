n=int(input())
st=str(input())
k=len(st)//n
nt=''
outs=''
for i in range(k):
    for j in range(n):
        nt+=st[(2*((i+1)%2)-1)*j+((i+1)//2)*n*2-i%2]
for i in range(n):
    for j in range(k):
        outs+=nt[i+j*n]
print(outs)