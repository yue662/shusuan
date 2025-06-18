import math
while True:
    try:
        n=str(input())
        check=0
        l=len(n)
        for i in range(math.ceil(l/2)):
            if int(n[i])!=int(n[l-1-i]):
                check=1
                break
        if check==0:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break