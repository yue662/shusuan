class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        outs=0
        for i in nums:
            outs^=i
        return outs