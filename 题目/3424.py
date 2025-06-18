import heapq
import math
n,m=map(int,input().split())
dic={}
for i in range(1,n+1):
    dic[i]=[]
for i in range(m):
    a,b,c=map(int,input().split())
    dic[a].append([b,c])
sl=[math.inf]*n
sl[0]=0
ks=[[0,1]]
ko=heapq.heappop(ks)
while True:
    for i in dic[ko[1]]:
        if i[1]+ko[0]<sl[i[0]-1]:
            sl[i[0]-1]=i[1]+ko[0]
            heapq.heappush(ks,[sl[i[0]-1],i[0]])
    ko=heapq.heappop(ks)
    while True:
        if ko[0]>sl[ko[1]-1]:
            ko=heapq.heappop(ks)
        else:
            break
    if ko[1]==n:
        print(ko[0])
        break