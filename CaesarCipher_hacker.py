print("Enter the message to hack")
message = input('>>> ')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?.,:;#@$%^&'


for key in range(len(SYMBOLS)):
    translate = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)

            num -= key

            if num < 0:
                num += len(SYMBOLS)

            translate += SYMBOLS[num]
        else:
            translate += symbol

    print('The decrypted message is: (key: {}) {}'.format(translate, key))