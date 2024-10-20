def caesar(texta, shifta, directiona):
    cipher=['']*len(texta)
    if directiona == 'encode':
        for i in range(len(texta)):
            if texta[i] in alphabet:
                    new_id = (alphabet.index(texta[i]) + shifta) % 26
                    cipher[i] = alphabet[new_id]
            else:
                cipher[i] = texta[i]

    elif directiona == 'decode':
        for i in range(len(texta)):
            if texta[i] in alphabet:
                new_id = (alphabet.index(texta[i]) - shifta) % 26
                cipher[i] = alphabet[new_id]
            else:
                cipher[i] = texta[i]
    print(''.join(cipher))




logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
while direction not in ['encode', 'decode']:
   print("Enter a valid direction")
   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")



text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(text, shift, direction)
inp=input("would you like to restart? (Type yes or no)").lower()
if inp == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    caesar(text, shift, direction)

else:
    print("Have a nice day!")





