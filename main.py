from tkinter import *
from PIL import Image, ImageTk
import vlc
import time
import pyperclip

morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.", "¿": "..-.-", "¡": "--...-"
}


def playsound():
    for code in morse_result:
        dot_sound = vlc.MediaPlayer("morse_sound/dot.ogg.mp3")
        dash_sound = vlc.MediaPlayer("morse_sound/dash.ogg.mp3")
        if code == ".":
            dot_sound.play()
        elif code == "-":
            dash_sound.play()
        elif code == "#":
            continue
        time.sleep(0.5)


def encode_text():
    global morse_result
    text = " ".join(text_input.get(1.0, "end-1c").upper().split())
    morse_result = ""
    for letter in text:
        if letter == " ":
            morse_result += "/ "
        else:
            morse_representation = morse_code.get(letter, "#")
            morse_result += f"{morse_representation} "

    text_output.config(text=morse_result.rstrip(), font=("Arial", 15, "normal"))


def copy_code():
    pyperclip.copy(morse_result.rstrip())


screen = Tk()
screen.config(pady=5)
screen.title("Morse Encode")

resize_image = Image.open("./image/play-svgrepo-com.png").resize((20, 20))
play_button_image = ImageTk.PhotoImage(resize_image)

text_input = Text(height=5, width=25, borderwidth=0)
text_input.grid(column=0, row=0, columnspan=2, padx=5)

morse_result = ""
text_output = Label(text=morse_result, wraplength=200)
text_output.grid(column=0, row=1, columnspan=2)

get_morse_button = Button(text="Encode", width=10, command=encode_text, background="sky blue", borderwidth=0)
get_morse_button.grid(column=0, row=2)

copy_text_button = Button(text="Copy", width=10, command=copy_code, background="sky blue", borderwidth=0)
copy_text_button.grid(column=1, row=2)

sound_button = Button(image=play_button_image, command=playsound, borderwidth=0)
sound_button.grid(column=2, row=0, padx=5)

screen.mainloop()
