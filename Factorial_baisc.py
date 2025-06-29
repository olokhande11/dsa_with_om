


# The factorial of a number (written as n!) means multiplying all the whole numbers from that number down to 1.

# Example:
# 5! (read as "five factorial") = 5 × 4 × 3 × 2 × 1 = 120

# 3! = 3 × 2 × 1 = 6

# 1! = 1


def factorial_basic(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result


a1 = input("Enter the Input of Which you want me to do factorial ")


val = int(a1)

print("result is {}".format(factorial_basic(val)))



