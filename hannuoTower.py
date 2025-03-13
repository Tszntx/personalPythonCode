def move(n,a,b,c):
    if n==1 :
        print(a,'-->',c)
        return 0
    elif n==2:
        A=a;B=c;C=b
        move(n-1,A,B,C)
        move(n-1,A,C,B)
        A=b;B=a;C=c
        move(n-1,A,B,C)
    else :
        A = a;
        B = c;
        C = b
        move(n - 1, A, B, C)
        move(1, A, C, B)
        A = b;
        B = a;
        C = c
        move(n - 1, A, B, C)
move(4,'A','B','C')