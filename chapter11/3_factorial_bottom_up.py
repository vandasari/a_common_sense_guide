"""
Calculate Factorial using Recursion with Bottom-up Strategy

Algorithm: page 167

Bottom-up approach --> implemented like the stack LIFO by the computer. 
"""


def factorial(n, i=1, product=1):
    if i > n:
        return product
    else:
        return factorial(n, i + 1, product * i)


# For displaying step-by-step execution:
def factorial_steps(n, i=1, product=1):
    print(f"i = {i}, product = {product} * {i} = {product * i}")
    if i > n:
        print(f"Base case: {i} > {n} - Returning {product}\n")
        return product
    else:
        print(f"Computing factorial of i = {i} or {i}!\n")
        value = factorial_steps(n, i + 1, product * i)
        print(f"Returning {i}! = {i} * {i-1}! = {i} * {product} = {product*i}")
        return value


if __name__ == "__main__":
    num = 5
    res = factorial(num)
    print(f"{num}! = {res}")

    print()

    num = 5
    factorial_steps(num)


"""
In this implementation, we have three parameters:
    - n: is the number whose factorial we’re computing. 
    - i: a simple variable that starts at 1 and increments by one in each 
      successive call until it reaches n. 
    - product: the variable in which we store the calculation as we keep 
      multiplying each successive number. 
      
We keep passing the product to the successive call so we can keep track of it 
as we go.

While we can use recursion in this way to achieve the bottom-up approach, it’s 
not particularly elegant and does not add much value over using a classic loop.
"""
