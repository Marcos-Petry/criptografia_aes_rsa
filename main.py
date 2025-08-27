from symmetric import encrypt_aes, decrypt_aes
from asymmetric import generate_keys, encrypt_rsa, decrypt_rsa
from Crypto.Random import get_random_bytes

def main():
    print("=== Sistema de Criptografia ===")
    print("1 - Criptografia Simétrica (AES)")
    print("2 - Criptografia Assimétrica (RSA)")
    opcao = input("Escolha a opção: ")

    if opcao == "1":
        key = get_random_bytes(16)
        text = input("Digite o texto para cifrar: ")
        enc = encrypt_aes(text, key)
        dec = decrypt_aes(enc, key)
        print(f"\nTexto cifrado (AES): {enc}")
        print(f"Texto decifrado (AES): {dec}")

    elif opcao == "2":
        private, public = generate_keys()
        text = input("Digite o texto para cifrar: ")
        enc = encrypt_rsa(text, public)
        dec = decrypt_rsa(enc, private)
        print(f"\nTexto cifrado (RSA): {enc}")
        print(f"Texto decifrado (RSA): {dec}")

    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
