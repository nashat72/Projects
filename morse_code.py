# create dirodictionary for morse code
morse_code_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
                    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
                    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
                    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                    "Y": "-.--", "Z": "--..", 
                    "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
                    ", ": "--..--", ".": ".-.-.-", "?": "..--..", "/": "-..-.", "-": "-....-", "(": "-.--.",
                    ")": "-.--.-"}

import numpy as np
import sounddevice as sd
import time

#coding
def text_to_morse (text):
    text = text.upper()
    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code = morse_code + morse_code_dict[char] + " "
    return morse_code

#decoding
def morse_to_text (morse):
    #reversing the dictionary
    reversed_morse_code_dict = {v:k for k, v in morse_code_dict.items()}
    text = ""
    for word in morse.split():
        if word in reversed_morse_code_dict:
            text = text + reversed_morse_code_dict[word] + ""
    return text

# Morse code sound generator
def play_morse(morse):
    frequency = 600  # sound frequency in Hz

    dot_duration = 0.1
    dash_duration = 0.3
    gap_duration = 0.1

    for symbol in morse:
        if symbol == ".":
            duration = dot_duration
        elif symbol == "-":
            duration = dash_duration
        elif symbol == " ":
            time.sleep(0.3)
            continue
        else:
            continue

        # Generate beep
        samples = np.arange(int(44100 * duration))
        beep = 0.5 * np.sin(2 * np.pi * frequency * samples / 44100)

        # Play beep
        sd.play(beep, 44100)
        sd.wait()
        time.sleep(gap_duration)

#main 
def main():
    #print the morse code list for information
    code_list = morse_code_dict.items()
    print("The Morse code is:")
    print(code_list)
    choice = input("Enter:\n1 to convert text to morse code\n2 to convert morse code to text\n= ")
    #if select to generate a morse code
    if choice == "1":
        text = input("Enter the text to convert to morse code: ")
        print("Morse code is: ", text_to_morse(text))
        # paly the beep
        play_morse(text_to_morse(text))
    # if select to retrun text    
    elif choice == "2":
        morse = input("Enter the morse code to convert to text: ")
        print("Text is: ", morse_to_text(morse))
    else:
        print("Invalid choice")

# call the function to start the code
main()
