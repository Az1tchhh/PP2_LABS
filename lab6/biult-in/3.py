def palindrome(str):
    
    if(  list(str) == list(reversed(str))  ):
        return True
    return False

print(palindrome("abba"))
print(palindrome("abb"))
print(palindrome("aa"))