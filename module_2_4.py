numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i > 1:
        for k in range(2, int(i ** 0.5) + 1):
            if i % k == 0:
                not_primes.append(i)
                break
        else:
            primes.append(i)
print(primes)
print(not_primes)


