myMessage = str(input())
cipher_list = myMessage.split()
cipher_message = ""
for i in range(len(cipher_list)):
    if(len(cipher_list[i])<3):
        continue
    else:
        cipher_message += cipher_list[i]
        cipher_message +=" "
print(cipher_message)