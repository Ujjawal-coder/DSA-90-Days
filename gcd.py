a=int(input())
b=int(input())

m,n = a,b
while m !=n:
    if m>n:
        m= m-n
    else:
        n= n-m
gcd = m

lcm = a * b // gcd
print(lcm)