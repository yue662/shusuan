sl=list(map(float,input().split()))
o=len(sl)
def f(a,x):
    t=a*x+1.1**(a*x)
    return t
def check(a):
    nl=[]
    k=0
    for i in sl:
        if f(a,i)>=85:
            k+=1
    if k/o>=0.6:
        return True
    else:
        return False
st=0
end=1000000000
while True:
    mid=(st+end)//2
    if check(mid/1000000000):
        end=mid
    else:
        st=mid+1
    if st>=end:
        break
print(end)