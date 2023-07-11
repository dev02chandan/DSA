def isPallindrome(string, start, end):
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


string = "abc"
print(string)
print(isPallindrome(string, 0, 0))
