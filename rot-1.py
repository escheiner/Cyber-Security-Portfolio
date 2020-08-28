#!/user/bin/python3

#Get mode, messsage, and key from the user
mode = input("Would you like to encrypt or decrypt? (encrypt or decrypt) ")
message = input("Please enter your message: ")
key = int(input("What is your secret key? (numbers only) "))

#Convert message to lowercase to manipulate and define abcs
message = message.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Create variable for transformed text
transformed_text = ""

#subtract key if user would like to decrypt the message
if mode == "decrypt":
    key = key * -1

#apply cipher
for char in message: 
    if char != ' ':
        print (alphabet[((alphabet.index(char))+ key)%26])
        transformed_text += alphabet[((alphabet.index(char) + key) % 26)]
    else:
        transformed_text += " "

print(transformed_text) 
