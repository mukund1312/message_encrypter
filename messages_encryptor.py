# Vigenere / Vernam / Ceasar Ciphers - Functions for encrypting and decrypting data messages.
# Then send them to a friend.


def vigenere():
    choice = int(input("1.To entrypt\n2.To decrpyt\n"))
    if(choice == 1):
        string_in = input("enter the string :\n")
        string_out = ""
        for i in string_in:
            string_out = string_out+chr((ord(i)+3))
        print(string_out)
    elif(choice == 2):
        string_in = input("enter the string :\n")
        string_out = ""
        for i in string_in:
            string_out = string_out+chr((ord(i)-3))
        print(string_out)
    else:
        print("invalid")


vigenere()
