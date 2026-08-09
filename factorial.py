def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Test cases
print(factorial(0))   # 1
print(factorial(1))   # 1
print(factorial(5))   # 120
print(factorial(7))   # 5040