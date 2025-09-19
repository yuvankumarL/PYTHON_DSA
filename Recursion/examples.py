
# Factorial
# Factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    # print('n', n)
    if n == 0:
        return 1
    else:
        # print('fact', factorial(n - 1))
        return n * factorial(n - 1) 
print(factorial(5))  # Output: 120
print('-------------------')

# Python Implementation Using Binet's Formula
import math

def fibonacci(n):
    
    # Golden ratio (φ) and its negative counterpart (ψ)
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2

    # Compute Fibonacci number using full Binet's formula
    return round((math.pow(phi, n) - math.pow(psi, n)) / math.sqrt(5))


if __name__ == "__main__":
    n = 5  # Example input
    print(f"Fibonacci({n}) =", fibonacci(n))

    n = 9
    print(f"Fibonacci({n}) =", fibonacci(n))