# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains

# reduce(function, iterable)

import functools

letters = ['H', 'E', 'L', 'L', 'O']
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

nums = [5, 4, 3, 2, 1]
factorial = functools.reduce(lambda x, y: x * y, nums)
print(factorial)

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

print(factorial(5))