#!/usr/bin/python3
'''
This module calculates the minimum number of times to copy H
'''


def minOperations(n: int) -> int:
    
    '''
        minOperations finds the min number of operations to copy n number of H
        arg: n
        returns the number of operations
    '''
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor ==0:
            operations += factor
            n //= factor
        factor += 1
    return operations
