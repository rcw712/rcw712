"""
A module for some interesting math functions

Copyright Brian E. Chapman, PhD
"""
import numpy as np
def gcd(a,b):
    """gcd: a function to compute the greatest common denominator of two integers

    Arguments:
        a: An integer greater than zero
        b: An integer greater than zero
    Returns:
        An integer that is the greatest common denominator of a, b 
        OR
        -1: If either a or b are not integers
        -2: If either a or b are non-positive integers

    """
    if not type(a)==int or not type(b)==int:
        return -1
    elif a <=0 or b <= 0:
        return -2
        
    
    # If a<b, exchange a and b.
    if a < b:
        temp = a
        a=b 
        b=temp
    # Divide a by b and get the remainder, r.
    r = a%b
    if r == 0:
        return b
    else:
        return gcd(b,r)
    #Else replace a by b and replace b by r.
    #return a,b

def sieve_primes(N=100):
    """Finds all the prime numbers less than or equal to N using the Sieve of Eratosthenes
    
    N: positive integer"""
    if N < 2: # No primes less than 2
        return []
    
    nums = np.arange(2,N+1).astype(np.int32)
    primes = []
    for i in range(len(nums)):
        if nums[i] != -1:
            primes.append(nums[i])
            nums[i+nums[i]::nums[i]] = -1
    return tuple(primes)
