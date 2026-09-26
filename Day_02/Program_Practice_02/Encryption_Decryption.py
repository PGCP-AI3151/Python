code ={'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h',
       'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n',
       'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't',
       'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 'v': 'y', 'w': 'z',
       'x': 'a', 'y': 'b', 'z': 'c'}


encryption = input("Enter Encryption :-")
decryption = ""

for ch in encryption:
   for key,value in code.items():
       if value == ch:
           decryption += key

print('Decrypted :',decryption)

