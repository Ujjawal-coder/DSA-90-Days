n=int(input())
m=int(input())
while n!=m:
    if n>m:
        n=n-m
    else:
        m=m-n
gcd=n

lcm = n*m/gcd
print(lcm)