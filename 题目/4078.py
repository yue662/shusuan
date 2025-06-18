import heapq
heap=[]
n=int(input())
for i in range(n):
    k=str(input())
    if '1' in k[0]:
        heapq.heappush(heap,int(k[2:]))
    else:
        o=heapq.heappop(heap)
        print(o)