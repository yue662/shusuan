n=int(input())
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in '*/+-':
            while opStack and (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)
        else:
            postfixList.append(token)
    while opStack:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
for _ in range(n):
    st=str(input())
    st1=''
    for i in st:
        if i in '()+-*/':
            st1+=' '+i+' '
        else:
            st1+=i
    print(infixToPostfix(st1))