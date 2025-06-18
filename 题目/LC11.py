class Solution:
    def maxArea(self, height: List[int]) -> int:
        nl=[]
        def cin(i,j):
            if i==j:
                return
            if height[i]<height[j]:
                nl.append(height[i]*(j-i))
                cin(i+1,j)
            else:
                nl.append(height[j]*(j-i))
                cin(i,j-1)
        cin(0,len(height)-1)
        return max(nl)