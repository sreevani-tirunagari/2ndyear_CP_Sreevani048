# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isprime(n):
    if (n < 2):
        return False
    if (n==2):
        return True
    else:
        for i in range(2,int(n)):
            if(n%i==0):
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
        
        if ((ishappynumber(guess)) and (isprime(guess))):
            found += 1
            
    return guess