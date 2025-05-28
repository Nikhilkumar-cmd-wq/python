def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char  
    return encrypted_message

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)  
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
encrypted = encrypt(message, shift)
print(f"Encrypted Message: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted Message: {decrypted}")