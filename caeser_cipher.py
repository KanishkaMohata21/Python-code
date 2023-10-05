alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    new_text=""
    for i in text:
        if i in alphabet:
            position=alphabet.index(i)
            new_position=position+shift
            new_letter=alphabet[new_position]
            new_text+=new_letter
        else:
            new_text+=i
    print(new_text)

def decrypt(text,shift):
    new_text=""
    for i in text:
        if i in alphabet:
            position=alphabet.index(i)
            new_position=position-shift
            new_letter=alphabet[new_position]
            new_text+=new_letter
        else:
            new_text+=i
    print(new_text)

while input("Do you want to encode or decode a message,Type y for yes or n for no:")=="y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)
    else:
        print("INVALID INPUT")

print("Thank you for using this app.")