# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
# print("All test cases passed... :-)")

def isPrime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
def revNumber(n):
    p=n
    rn = 0
    while(n!=0):
        rm = n%10
        rn = rn*10 + rm
        n = n//10
    return (rn==p)

def isPalindromePrime(n):
    if (isPrime(n)==True) and (revNumber(n)==True):
        return True
    return False


print(isPalindromePrime(131))