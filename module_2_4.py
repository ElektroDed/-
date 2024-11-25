numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for k in range(2, i+1):
        if i % k == 0 and i != k:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True and i != 1:
        primes.append(i)
    if is_prime == False and i != 1:
        not_primes.append(i)
print (primes)
print (not_primes)
