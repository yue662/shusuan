class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        sl=[]
        for i in range(n):
            sl.append(ord(s[i]))
        dp=[]
        for j in range(n):
            dp.append([0]*(j+1))
        for z in range(n):
            dp[z][z]=1
        for c in range(1,n):
            if sl[c]==sl[c-1]:
                dp[c][c-1]=2
        for k in range(2,n):
            for l in range(k-1):
                if sl[l]==sl[k] and dp[k-1][l+1]!=0:
                    dp[k][l]=dp[k-1][l+1]+2
        out=[0,0,0]
        for o in range(n):
            for p in range(o):
                if dp[o][p]>out[2]:
                    out=[p,o,dp[o][p]]
        return s[out[0]:out[1]+1]