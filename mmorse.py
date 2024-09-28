morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

message = input("Type a message to translate into Morse code: ")

import random

def play_game():
    score = 0
    letters = list(morse_code_dict.keys())
    random.shuffle(letters)
    
    for letter in letters:
        if letter == ' ':
            continue
        print(f"What is the Morse code for {letter}?")
        answer = input("Your answer: ")
        if answer == morse_code_dict[letter]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {morse_code_dict[letter]}")
    
    print(f"Game over! Your score is {score}")

play_game()
