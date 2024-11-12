numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = 0
    for k in numbers:
        if i % k == 0 or i / k == 1:
            is_prime = is_prime + 1
        if i == k:
            break
    if is_prime == 2:
        primes.append(i)
    if is_prime > 2:
        not_primes.append(i)
print (primes)
print (not_primes)
