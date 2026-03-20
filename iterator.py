def multiplu_two_numbers(x, y):
    while x > 0:
        yield x*y
        yield x**2
        x -= 1


# we are creating an iterator here

a = multiplu_two_numbers(5, 2)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
