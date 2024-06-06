def pallindromestr(string):
    return string == string[::-1]

def pallindromestr(string):

    if len(string) < 2:
        return True
    
    if string[0] == string[-1]:
        return pallindromestr(string[1:-1])
    
    return False


# Leetcode
import string

def isPalindrome(s: str) -> bool:
        s = s.replace(' ', '')
        s = s.lower()
        trans = str.maketrans('', '', string.punctuation)
        s = s.translate(trans)
        return s == s[::-1]


print(isPalindrome('A man, a plan, a canal: Panama'))

# print(pallindromestr("asdfsdfdfsdfsafdasd"))
# print(pallindromestr("ABCDCBA"))