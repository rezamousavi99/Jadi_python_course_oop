def is_even(n):
    if n % 2 == 0:
        return True
    return False

first = 1
second = 2
fsum = 0
while first < 4000000:
    if is_even(first):
        fsum += first
    last = first + second
    first = second
    second = last

print(fsum)

