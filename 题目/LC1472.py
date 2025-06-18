class BrowserHistory:
    sl=[]
    check=0
    def __init__(self, homepage: str):
        BrowserHistory.sl=[homepage]
        BrowserHistory.check=0
    def visit(self, url: str) -> None:
        BrowserHistory.sl=BrowserHistory.sl[:(BrowserHistory.check+1)]
        BrowserHistory.check+=1
        BrowserHistory.sl.append(url)
    def back(self, steps: int) -> str:
        if BrowserHistory.check-steps>=0:
            BrowserHistory.check-=steps
            return BrowserHistory.sl[BrowserHistory.check]
        else:
            BrowserHistory.check=0
            return BrowserHistory.sl[0]
    def forward(self, steps: int) -> str:
        if BrowserHistory.check+steps<=len(BrowserHistory.sl)-1:
            BrowserHistory.check+=steps
            return BrowserHistory.sl[BrowserHistory.check]
        else:
            BrowserHistory.check=len(BrowserHistory.sl)-1
            return BrowserHistory.sl[len(BrowserHistory.sl)-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)