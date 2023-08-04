# print prime numbers from 1 to 10000

# is a number prime or not?
def is_prime(n):
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
    return prime


prime_sum = 0
for i in range(1, 10001):
    if is_prime(i):
        prime_sum += 1
        (last_prime_number := i)
        print(i, end=' ')

print(
    f'\nsum of prime ---> {prime_sum}\nlast prime number ---> {last_prime_number}')


