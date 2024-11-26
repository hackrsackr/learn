nums: int = range(1 , 1000)

def isPrime(num: int) -> bool:
    for x in range(2 , num):
        if (num % x) == 0:
            return False
    return True

primes: filter = filter(isPrime, nums)


print(list(primes))