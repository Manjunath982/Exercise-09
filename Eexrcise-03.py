def translate_to_secret_code(message, shift):
    secret_code = []

    for char in message:
        if char.isalpha():  # Check if the character is alphabetic
            start = ord('a') if char.islower() else ord('A')  # Determine starting ASCII value ('a' or 'A')
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            secret_code.append(shifted_char)
        else:
            secret_code.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(secret_code)


# Example usage:
message = input("Enter a message to translate into secret code language: ")
shift_amount = int(input("Enter the shift amount for the secret code: "))

translated_message = translate_to_secret_code(message, shift_amount)
print("Translated message:", translated_message)
