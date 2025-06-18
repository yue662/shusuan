import math
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(n):
            k=sum(math.ceil(i/n)-1 for i in nums)
            if k<=maxOperations:
                return True
            else:
                return False
        st=1
        ed=max(nums)+1
        outs=0
        while st<ed:
            mid=(st+ed)//2
            if check(mid):
                ed=mid
                outs=mid
            else:
                st=mid+1
        return outs