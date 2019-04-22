#VB
alphabet = "zJcDeFIHiBkLVNoPqRsTuxwXyZAbCdEfGhgjKlMnOpQrStUvWmYa1234567890`~!@#$%^&*()-_=+[{]}|;:',<.>/?" #Missing \ and "
key = 30
newMessage = ''
message = input('Please enter a message: ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position - key) % 92
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character
print(newMessage)