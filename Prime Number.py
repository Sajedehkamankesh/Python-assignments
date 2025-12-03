for a in range(2,100):
    p=1
    for i in range(2,int(a/2)+1):
        if a%i==0:
            p=0
            break
    if p==1:
            print(a)