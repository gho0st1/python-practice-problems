### Problem-5: Fibonacci Using Memoization

from functools import lru_cache

@lru_cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def add_suffix(n: int) -> str:
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

num = 50
# num = int(input("Enter a number: "))

print(f"The {add_suffix(num)} fibonacci number is {fibonacci(num)}")