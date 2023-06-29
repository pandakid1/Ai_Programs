# The following program implements the diffie-hellman algorithm
# Function to encode a message
def encrypt(message, key):
    cipher = ""
    for c in range(len(message)):
        number = ord(message[c])
        number += key
        cipher += chr(number)
    return cipher


# Function to decode a message
def decrypt(ciphertext, key):
    message = ""
    for c in range(len(ciphertext)):
        number = ord(ciphertext[c])
        number -= key
        message += chr(number)
    return message


# Function to find the shared key
def find_shared_key(private_key, public_key):
    shared_key = public_key ** private_key % public_modulus
    return shared_key


# Private Information
alice_private_key = 5
bob_private_key = 7
alice_message = "Hello Bob"

# Public Information
public_base = 8
public_modulus = 29
alice_public_key = public_base ** alice_private_key % public_modulus
bob_public_key = public_base ** bob_private_key % public_modulus

# Alice sends Bob an encrypted message
alice_shared_key = find_shared_key(alice_private_key, bob_public_key)
alice_cipher = encrypt(alice_message, alice_shared_key)
print(alice_cipher)

# Bob receives message and decrypts using shared key
bob_shared_key = find_shared_key(bob_private_key, alice_public_key)
bob_message = decrypt(alice_cipher, bob_shared_key)
print(bob_message)