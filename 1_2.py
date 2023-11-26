n=12012
m=n
counter=0
while n!=0:
    if m**2<=n:
        n-=m**2
        counter+=1
    elif m>1:
        m-=1
print(counter)




