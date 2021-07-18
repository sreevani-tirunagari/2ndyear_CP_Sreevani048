# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
    a = abs(n)
    if a == 0:
        return 0
    else:
        while(a>0):
            num=a
            res1 = num%10
            num = num//10
            res2= num%10
            if(res1 != res2 and a>9):
                a=a//10
            else:
                return res1
        return min(res1,res2)
