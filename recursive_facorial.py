

def rec_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1  # Base case
    return n * rec_factorial(n - 1)
    


a1 = input("Enter the Input of Which you want me to do factorial ")


val = int(a1)

print("result is {}".format(rec_factorial(val)))
