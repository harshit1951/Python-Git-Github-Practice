def solve(n):
    num = 0
    while(n > 0):
        num = num*10 + n%10
        n = n//10
        
    return num

x = solve(212)

if x == 212:
    print("Palindrome")
else:
    print("Not Palindrome")


