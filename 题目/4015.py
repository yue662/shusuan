while True:
    try:
        st=str(input()).strip()
        n=st.count('@')
        sl=[st[0],st[-1]]
        if n==1 and '@' not in sl and '.' not in sl:
            k=st.index('@')
            if st.count('.',k,len(st)-1)>=1 and st[k-1]!='.' and st[k+1]!='.':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    except EOFError:
        break