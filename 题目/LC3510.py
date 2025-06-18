class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ci=0
        while True:
            if len(nums)==1:
                break
            all = nums[0] + nums[1]
            z = 0
            t = 0
            now = nums[0]
            for i in range(len(nums) - 1):
                if t==0:
                    if nums[i] < now:
                        t = 1
                now = nums[i]
                if nums[i] + nums[i + 1] < all:
                    all = nums[i] + nums[i + 1]
                    z = i
            if nums[-1] < now:
                t = 1
            if t == 0:
                break
            nums[z]=nums[z]+nums[z+1]
            del nums[z+1]
            ci+=1
        return ci