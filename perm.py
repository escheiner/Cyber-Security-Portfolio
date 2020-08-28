#!/user/bin/python3
def permutation(key, mode):
    #alphabetize key
    sorted_key = "".join(sorted(key))
    perm = []
    #Create permutation by taking index of char, then delete char.
    if mode == 'decrypt': 
        for char in sorted_key:
            perm.append(key.index(char))
            key = key.replace(char,'.',1)
    elif mode == 'encrypt':
        for char in key:
            perm.append(sorted_key.index(char))
            sorted_key = sorted_key.replace(char, '.',1)
    else: 
        print("You have not selected a valid mode. Please select encrypt or decrypt.")
    return perm


def format_msg(str, n):
    #strip string of white spaces and convert to uppercase
    str = str.replace(" ", '')
    str = str.upper()
    #split string into chunks the size of the key length
    chunks = [str[i:i+n] for i in range(0, len(str), n)]
    #fill extra element with more xs
    for i in range(n - len(chunks[len(chunks)-1])):
        chunks[len(chunks)-1] =  chunks[len(chunks)-1] + "X"
    return chunks

def permute(perm, msg): 
    permuted_txt= ""
    print(perm)
    #swap letters in message based on permutation
    for chunk in msg: 
        for ind in perm: 
            permuted_txt += chunk[ind]
        permuted_txt += " "
    return permuted_txt
             


if __name__ == '__main__':
    #Get mode, key, and message from the user
    mode = input("Would you like to encrypt or decrypt? (encrypt or decrypt) ")
    message = input("Enter the message here: ")
    key = input("Enter the key here ")
    perm = permutation(key, mode)
    msg_chunks = format_msg(message, len(key))
    permuted_txt = permute(perm, msg_chunks)
    print(permuted_txt)
  

    