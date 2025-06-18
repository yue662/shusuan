from functools import lru_cache
@lru_cache
def ES(n):
  isprime=[True for _ in range(n+1)]
  prime=[]
  for i in range(2,n+1):
      if isprime[i]:
          prime.append(i)
      for j in range(len(prime)):
          if  i*prime[j]>n:break
          isprime[i*prime[j]]=False
          if i%prime[j]==0 :break
  return prime
sl=ES(10000)
dl=[]
for i in sl:
    if str(i)[-1] not in '1':
        dl.append(i)
for j in dl:
    sl.remove(j)
t=int(input())
for i in range(t):
    n=int(input())
    print('Case'+str(i+1)+':')
    zl=[]
    for j in sl:
        if j<n:
            zl.append(j)
    if len(zl)==0:
        print('NULL')
    else:
        print(*zl)