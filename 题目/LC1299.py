class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrs=sorted(arr,reverse=True)
        outs=[]
        for i in range(len(arr)-1):
            arrs.remove(arr[i])
            outs.append(arrs[0])
        outs.append(-1)
        return outs