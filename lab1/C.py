def toLowercase(s):
    second_string = ""
    for i in range(len(s)):
        if(s[i]>='0' and s[i]<='9'):
            second_string += s[i]
        elif (s[i] == s[i].upper()):
            cnt = ord(s[i])
            small_word = chr(cnt + 32)
            second_string += small_word
        else:
            second_string += s[i]
    return second_string


s = str(input())
print(toLowercase(s))