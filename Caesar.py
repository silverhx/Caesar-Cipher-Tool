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
    # ANSI Colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    print(BLUE + "===============================" + RESET)
    print(CYAN + "  Caesar Cipher Tool Made By - Deepak" + RESET)
    print(BLUE + "===============================" + RESET)
    print()

    print(YELLOW + "1. Encrypt" + RESET)
    print(YELLOW + "2. Decrypt" + RESET)
    
    choice = input(GREEN + "Choose an option (1/2): " + RESET).strip()

    if choice not in ['1', '2']:
        print(RED + "Invalid choice!" + RESET)
        return 

    message = input(GREEN + "Enter your message: " + RESET)
    shift = int(input(GREEN + "Enter shift value (e.g., 3): " + RESET))

    if choice == '1':
        print(BLUE + "\nEncrypted Message:" + RESET, GREEN + caesar_cipher(message, shift, 'encrypt') + RESET)
    elif choice == '2':
        print(BLUE + "\nDecrypted Message:" + RESET, GREEN + caesar_cipher(message, shift, 'decrypt') + RESET)


if __name__ == "__main__":
    main()
