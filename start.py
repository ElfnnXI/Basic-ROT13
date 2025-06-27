import codecs

def rot13(text):
    return codecs.encode(text, 'rot_13')

if __name__ == "__main__":
    print("=== ROT13 Cipher ===")
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Enter your choice (1/2): ")

    if choice in ['1', '2']:
        message = input("Enter the message: ")
        result = rot13(message)
        print(f"Result: {result}")
    else:
        print("Invalid choice. Exiting.")
