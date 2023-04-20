import pyfiglet

# Create header
course = input("What's your course? ")
print(pyfiglet.figlet_format(f"Welcome, {course} student!", font="larry3d", width=80))
print("=" * 20)
print("\033[34mDecrypt the message!\033[0m")
print("=" * 20)

# Define the character substitution dictionary
char_map = {'*': 'a', '&': 'e', '#': 'i', '+': 'o', '!': 'u'}

# Define the decryption function
def decrypt(ciphertext):
    plaintext = ''
    for c in ciphertext:
        plaintext += char_map.get(c, c)
    print("\033[33m\033[0m", plaintext)

# Prompt the user for input and decrypt it
while True:
    ciphertext = input("Enter the message to decrypt: ")
    decrypt(ciphertext)
    
    choice = input("\"Do you want to decrypt another message? (y/n): ")
    if choice.lower() == "n":
        print("Exiting program. Goodbye!")
        break
    elif choice.lower() == "y":
        continue
    else:
        print("Invalid input, will exit the program. Goodbye!")
        break
