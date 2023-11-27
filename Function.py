
print("Welcome to my application!")
print("This is a morse code application")
print("Reminder a space between words or characters will be defined by '/'.")
def encryption(message):
    encoded_message = " "
    alphabet_to_morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'}
    encoded_message = " ".join(alphabet_to_morse_dict.get(c,'') for c in message.upper())
    if message == "":
        print("No input. Text is needed to ouput")
    return encoded_message


# message = input("Enter messege to encrypt: ")
# print(encryption(message))


def decryption(message):
    decoded_message = " "
    morse_to_alphabet_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
    '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
    '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@', '/': ' '}
    decoded_message = "".join(morse_to_alphabet_dict.get(c, '') for c in message.split())
    return decoded_message


# message = input("Enter messege to decrypt: ")
# print(decryption(message))


# def invalid_input():
#     print("Invalid Input")
# def print_invalid_input():
#     print("Invalid input. Please try again.")

while True:
    choice = input("Choose 0 for exit, 1 for Encrypt, 2 for Decrypt: ")
    if choice == '0':
        break
    elif choice == '1':
        message = input("Enter messege to encrypt: ")
        print(encryption(message))
    elif choice == '2': 
        message = input("Enter messege to decrypt: ")
        print(decryption(message))                                  #Add a line that says en law fy morse code 8alat ytal3a y ignore el heta dy.
    else: 
       print("Invalid input")               
# 
# 
#  # EL HETA DY 8ALAT  
# #     
#    #I want this to be a function 



#  #3ayza law arabic yedy this character is wrong w 3ayza amel lel invalid input a function, w yamely raise error. 