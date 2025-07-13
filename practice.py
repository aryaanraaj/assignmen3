n = int(input("Enter your choice: "))

def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers."
    elif n==0 or n==1:
        return 1
    else:
        f = n * (factorial(n-1))
        return f

ans = factorial(n)
print("factorial of", n , "is:",ans)
