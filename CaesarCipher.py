SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print('')

while True:
    print('Do you want to encrypt(e) or decrypt(d): ')
    response = input('>>> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Enter e or d!')


while True:
    maxkey = len(SYMBOLS) - 1

    print('Enter the key to use')
    response1 = input('>>> ').upper()

    if not response1.isdecimal():
        continue

    key = int(response1)

    if 0 <= key <=maxkey:
        break
    else:
        print(f'Please enter a key between 0 and {maxkey}')

print('Enter the message to {}'.format(mode))

message = input('>>> ').upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)


        translated += SYMBOLS[num]

    else:
        translated += symbol


print(translated)