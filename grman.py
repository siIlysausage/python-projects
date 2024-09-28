english_to_irish = {
    'hello': 'dia dhuit',
    'goodbye': 'slán',
    'please': 'le do thoil',
    'thank you': 'go raibh maith agat',
    'yes': 'tá',
    'no': 'níl',
    'cat': 'cat',
    'dog': 'madra',
    'milk': 'bainne',
    'food': 'bia' ,
    'car': 'carr' ,
    'march': 'marta',
    'box' : 'bosca',
    'lunch' : 'lon',
    'pizza' : 'piotza',  }

message = input("Enter a word or phrase to translate into Irish: ").lower()

translated_message = " ".join(english_to_irish.get(word, word) for word in message.split())
print("Irish Translation:", translated_message)
