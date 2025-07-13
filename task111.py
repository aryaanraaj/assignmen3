import math

user = float(input("Enter your a number: "))

if user < 0:
    print("Square root and logarithm are not defined for negative numbers.")
else:
    sqrt_result = math.sqrt(user)
    log_result = math.log(user)  
    print("square root: ",sqrt_result)
    print("logarithm: ",log_result)

sine_result = math.sin(user)
print("sine", sine_result)
