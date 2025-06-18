class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nl=[0]
        min=prices[0]
        for i in range(len(prices)-2):
            if prices[i]<=prices[i+1]>prices[i+2]:
                nl.append(prices[i+1]-min)
            elif prices[i+1]<min:
                min=prices[i+1]
        nl.append(prices[-1]-min)
        return max(nl)