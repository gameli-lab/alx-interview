#!/usr/bin/python3

''' Primes game module'''


def isWinner(x, nums):
    ''' isWinner method to determin who wins the prime game'''
    max_n = max(nums) if nums else 0
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    ''' Sieve of Erastosthenes to find all primes up to max_n'''
    for start in range(2, int(max_n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, max_n + 1, start):
                is_prime[multiple] = False

    '''Counting the total number of primes to the number given'''
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria = 0
    ben = 0

    '''Since Maria goes first, she wins on odd prime numbers else Ben wins on
    even primes'''
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
