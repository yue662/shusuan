def en(sl,nl,outs):
    n=len(sl)
    m=len(nl)
    if n==0:
        outs.append(nl)
    else:
        for i in range(n):
            zl=nl.copy()
            ol=sl.copy()
            nl.append(sl[i])
            del sl[i]
            en(sl,nl,outs)
            nl=zl
            sl=ol
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s=len(nums)
        if s==1:
            return [nums]
        else:
            outs=[]
            for i in range(s):
                sl=nums.copy()
                del sl[i]
                en(sl,[nums[i]],outs)
        return outs
a=Solution()
print(a.permute([1,2,3]))