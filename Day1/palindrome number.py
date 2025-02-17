n = int(input())
rev = 0
temp = n 

while temp != 0:
    pal= temp%10
    rev = rev * 10 + pal
    temp = temp//10
    
if rev ==n :
    print("palindrome")
else:
    print("not a palindrome")