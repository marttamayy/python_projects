import logocaesar

print(logocaesar.logo)

while True:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Keep asking for input until the user provides a valid one
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        
        if direction == "encode" or direction == "decode":
            break  # Exit the loop when valid input is given
        elif direction == "close":
            print("Exiting the program.")
            exit()  # Exit the programa
        else:
            print("Please enter a valid action: 'encode' | 'decode' \nOr type 'close' to exit the code")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    def caesar(text, shift, direction):
        result_text = ""
        result = ""

        if direction == "encode":
            for letter in text:
                if letter in alphabet:
                    # Find the position of the letter in the alphabet
                    pos_letter = alphabet.index(letter)
                    # Calculate the new position using the shift
                    new_pos_letter = (pos_letter + shift) % 26
                    # Append the shifted letter to result_text
                    result_text += alphabet[new_pos_letter]
                else:
                    # If the letter is not in the alphabet, add it unchanged
                    result_text += letter
            
            result = (f"The encoded text is {result_text}")

        if direction == "decode":
            for letter in text:
                if letter in alphabet:
                    # Find the position of the letter in the alphabet
                    pos_letter = alphabet.index(letter)
                    # Calculate the new position using the shift
                    new_pos_letter = (pos_letter - shift)%26
                    # Append the shifted letter to result_text
                    result_text += alphabet[new_pos_letter]
                else:
                    # If the letter is not in the alphabet, add it unchanged
                    result_text += letter
            
            result = (f"The decoded text is {result_text}")
        

        return result

    # ---- old ------

    # def encrypt(text, shift):
    #     result_text = ""

    #     for letter in text:
    #         if letter in alphabet:
    #             # Find the position of the letter in the alphabet
    #             pos_letter = alphabet.index(letter)
    #             # Calculate the new position using the shift
    #             new_pos_letter = pos_letter + shift
    #             # Append the shifted letter to result_text
    #             result_text += alphabet[new_pos_letter]
    #         else:
    #             # If the letter is not in the alphabet, add it unchanged
    #             result_text += letter
        
    #     return result_text

    #Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

    # def decrypt(text, shift):
    #     result_text = ""

    #     for letter in text:
    #         if letter in alphabet:
    #             # Find the position of the letter in the alphabet
    #             pos_letter = alphabet.index(letter)
    #             # Calculate the new position using the shift
    #             new_pos_letter = pos_letter - shift
    #             # Append the shifted letter to result_text
    #             result_text += alphabet[new_pos_letter]
    #         else:
    #             # If the letter is not in the alphabet, add it unchanged
    #             result_text += letter
        
    #     return result_text

    # if direction == "encode":
    #     result = caesar(text,shift)
    #     print(f"The decoded text is {result}")
    # elif direction == "decode":
    #     result = caesar(text,shift)
    #     print(f"The decoded text is {result}")
    # else:
    #     print("Please enter a valid action: encode | decode")

    caesar_result = caesar(text, shift, direction)
    print(caesar_result)

    # Loop for asking if the user wants to cipher another text
    while True:
        keep_running = input("Do you want to cypher another text?\nType 'yes' or 'no': ").lower()

        if keep_running == "yes":
            break  # Restart the main loop for another round
        elif keep_running == "no":
            print("Exiting the program.")
            exit()  # End the program
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
