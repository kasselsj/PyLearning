def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True

def get_primes(max_number):
    list_of_primes = []
    for i in range (2,max_number):
        if is_prime(i):
            list_of_primes.append(i)
    return list_of_primes

max_num = int(input("Search for prime numbers up to: "))

list_of_primes = get_primes(max_num)
for prime in list_of_primes:
    print(prime)