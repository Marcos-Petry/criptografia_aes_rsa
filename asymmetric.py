from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa(message, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_rsa(encrypted_message, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted.decode('utf-8')

if __name__ == "__main__":
    private, public = generate_keys()
    text = "Criptografia RSA funcionando!"
    enc = encrypt_rsa(text, public)
    dec = decrypt_rsa(enc, private)
    print("Texto original:", text)
    print("Texto cifrado (RSA):", enc)
    print("Texto decifrado:", dec)
