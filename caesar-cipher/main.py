from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):

    result = ""

    if direction == 'decode':
        shift *= -1

    for letter in text:

        shifted_index = alphabet.index(letter) + shift

        if (shifted_index >= 26) or (shifted_index < 0):
            shifted_index = shifted_index % 26
        
        result += alphabet[shifted_index]
    
    if direction == 'encode':
        print(f"The encoded text is:  {result}")
    elif direction == 'decode':
        print(f"The decoded text is:  {result}")

end_program = False

while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:  ")
    text = input("Type your message:  ").lower()
    shift = int(input("Type the shift number:  "))

    caesar(text, shift, direction)
    
    end = input("Enter 'y' to restart, any other key to end:  ").lower()
    if end != 'y':
        end_program = True
        print("Ending program!")