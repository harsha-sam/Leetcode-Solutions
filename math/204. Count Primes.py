class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for i in range(n)]
        p = 2
        while p * p < n:
            if primes[p] == True:
                for i in range(p * p, n, p):
                    primes[i] = False
            p += 1
        return len([i for i in range(2, n) if primes[i] == True])