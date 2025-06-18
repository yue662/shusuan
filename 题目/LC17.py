dic={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        sl=[['']]
        k=len(digits)
        for i in range(k):
            sl.append([])
            for j in sl[i]:
                for s in dic[int(digits[i])]:
                    sl[i+1].append(str(j+s))
        return sl[-1]