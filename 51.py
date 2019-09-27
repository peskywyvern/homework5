sentence = input('Sentence: ')
symbol = input('Symbol to remove: ')
for character in sentence:
    if character == symbol:
        sentence = sentence.replace(symbol, '')
print(sentence)