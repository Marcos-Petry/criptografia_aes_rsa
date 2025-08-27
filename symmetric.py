from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_aes(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_aes(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message)).decode('utf-8')
    return decrypted.strip()

if __name__ == "__main__":
    key = get_random_bytes(16)
    text = "Segurança é importante!"
    enc = encrypt_aes(text, key)
    dec = decrypt_aes(enc, key)
    print("Texto original:", text)
    print("Texto cifrado (AES):", enc)
    print("Texto decifrado:", dec)