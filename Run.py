import argparse
import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="File encryption and decryption using AES.")
    parser.add_argument("-en", action="store_true", help="Encryption")
    parser.add_argument("-de", action="store_true", help="Decryption")
    parser.add_argument("-k", "--key", help="Encryption/Decryption key")
    parser.add_argument("input_file", help="The name of the input file")
    parser.add_argument("output_file", help="The name of the output file")
    args = parser.parse_args()

    if args.en:
        if args.key:
            key = base64.urlsafe_b64encode(args.key.encode())
        else:
            key = generate_key()
        encrypt_file(key, args.input_file, args.output_file)
        print("Encryption complete.")
        print("Key: ", key.decode())  # Wypisz klucz dla informacji
    elif args.de:
        if args.key:
            key = base64.urlsafe_b64encode(args.key.encode())
        else:
            key = input("Enter the decryption key: ")
        decrypt_file(key, args.input_file, args.output_file)
        print("Decryption complete.")
    else:
        print("You need to select the mode: -en (encryption) or -de (decryption)")

if __name__ == "__main__":
    main()
