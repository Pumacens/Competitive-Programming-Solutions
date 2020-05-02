
# Code to generated prime factors here:
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors

def find_key(encryption_key):
    n = int(encryption_key, 16)
    result = 1
    prime_facts = []
    for i in range(2,n):
        while n % i == 0:
            n = n//i
            prime_facts.append(i)
    
        if n == 1: 
            break
    
    if n > 1: prime_facts.append(n)
    return (prime_facts[0]-1)  *  (prime_facts[1]-1)



# def find_key(key):
#     n = int(key, 16)
#     return next((k - 1) * ((n // k) - 1) for k in range(2, int(n**0.5)+1) if n % k == 0)