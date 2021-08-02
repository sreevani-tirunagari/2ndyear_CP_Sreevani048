
  
# // Write the method vowelCount(s), that takes a string s, 
# // and returns the number of vowels in s, ignoring case, 
# // so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
# // So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).


def vowelCount(s):
    count = 0
    s = s.lower()
    for ch in s:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count

print(vowelCount("orange"))