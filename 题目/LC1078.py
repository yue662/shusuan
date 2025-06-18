class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        sl=list(map(str,text.split()))
        nl=[]
        for i in range(len(sl)-2):
            if sl[i]==first and sl[i+1]==second:
                nl.append(sl[i+2])
        return nl