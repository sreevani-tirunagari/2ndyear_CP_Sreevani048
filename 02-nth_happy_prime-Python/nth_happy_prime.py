# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True


def ishappynumber(n):
    
    if n<1:
        return False
    sum = 0
    while(n>0):
        sum+= (n % 10) * (n % 10)
        n = n//10
    if sum == 1:
        return True 
    elif sum == 4:
        return False
    else:
        return ishappynumber(sum)

def fun_nth_happy_prime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        
        if ((ishappynumber(guess)) and (isPrime(guess))):
            found += 1
            
    return guess