class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        lk=[1]*n
        k=1
        for i in range(n-1):
            if nums[i+1]-nums[i]>maxDiff:
                k+=1
            lk[i+1]=k
        result=[]
        for qu in queries:
            if lk[qu[0]]==lk[qu[1]]:
                result.append(True)
            else:
                result.append(False)
        return result