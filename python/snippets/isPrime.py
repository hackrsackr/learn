nums = range(1 , 1000)

def isPrime(num: int) -> bool:
    for x in range(2 , num):
        if (num % x) == 0:
            return False
    return True

def isEven(num: int) -> bool:
    if (num % 2) != 0:
        return False
    return True

# filter returns a memory efficient object 
# filter(function or none, iterable)
primes = filter(isPrime, nums)

# print(primes)
print(list(primes))

evens = filter(isEven, nums)

# print(evens)
print(list(evens))