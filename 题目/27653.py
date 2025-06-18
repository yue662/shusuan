a1,b1,a2,b2=map(int,input().split())
c1=a1*b2+b1*a2
c2=b1*b2
def gcd(a, b):
  while b:
    a, b = b, a%b
  return a
o=gcd(c1,c2)
c1=int(c1/o)
c2=int(c2/o)
if c1==0:
    print('0/1')
else:
    print(str(c1)+'/'+str(c2))