def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  
    
    for char in text:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char 
    return result


def main():
    print("Caesar Cipher Tool Made By - Deepak")
    print()
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Choose an option (1/2): ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice!")
        return 

    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == '1':
        print("\nEncrypted Message:", caesar_cipher(message, shift, 'encrypt'))
    elif choice == '2':
        print("\nDecrypted Message:", caesar_cipher(message, shift, 'decrypt'))


if __name__ == "__main__":
    main()
