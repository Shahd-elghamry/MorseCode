
print("\nWelcome to my application!")
print("This is a morse code application")
print("Reminder a space between words or characters should be defined by '/' ")    # Should add this for when decrypting a message
print("When encryption be advised '.' and '-' are characters in the dictionary therefore it will be encryptd.")   # this is added for when encrypting user should be advised that dots and dashes will be encrypted.



def encryption(message):      # created functions to be able to do the unittesting
    encoded_message = " "          # had to define the variable 
    alphabet_to_morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'}                                    # dictionary for alphabet to morse
    encoded_message = " ".join(alphabet_to_morse_dict.get(c,'') for c in message.upper())                   # empty string is there for when we join the results it joins there.
    if message == "":
        print("\nNo input. Text is needed to ouput")                  # in case input wasn't added
    return encoded_message                  # at the end of the function return should be added. 



def decryption(message):                # Function for decrypting 
    decoded_message = " "           # same as encrypting
    morse_to_alphabet_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
    '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
    '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
    '...-..-': '$', '.--.-.': '@', '/': ' '}
    decoded_message = "".join(morse_to_alphabet_dict.get(c, '') for c in message.split())       # for every character in dictionary get it for every character in message
    if message == "":
        print("\nNo input. Morse code is needed to ouput")
    return decoded_message



def invalid_input():            # Function for invalid input
    message = " "
    if message == " ":
        print("\n Invalid input. Please enter a valid option.\n")



while True:             # while loop to make it run forever until told othersie
    choice = input("\nChoose 0 for exit, 1 for Encrypt, 2 for Decrypt: ")
    if choice == '0':   
        print("\nThank you for using the Morse code application. \n")                                                    
        break                                       # Program stops running 
    elif choice == '1':
        message = input("\nEnter messege to encrypt: \n")
        print("\nThis is your encrypted text: \n", encryption(message))
    elif choice == '2': 
        message = input("\n Enter messege to decrypt: \n")
        print("\nThis is your decrypted text: \n", decryption(message))                          
    else: 
        invalid_input()