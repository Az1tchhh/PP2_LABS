count = int(input())
array_of_strings = []
for i in range(count):
    Emails = str(input())
    if "@gmail.com" in Emails:
        array_of_strings.append(Emails[:(len(Emails)-10)])
for i in range(len(array_of_strings)):
    print(array_of_strings[i])
