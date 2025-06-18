class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if target>nums[-1]:
                return len(nums)
            else:
                for i in range(10**5):
                    if target+i in nums:
                        return nums.index(target+i)
                        break