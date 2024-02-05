# MorseCode-encode
_I am a junior Python developer. I will upload my portfolio on this GitHub account. Feel free to give suggestions on my portfolio, such as improving the code or providing some additional features. It will make me very happy and will improve my programming skills._

## Introduction
Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs [(Wikipedia)](https://en.wikipedia.org/wiki/Morse_code#). The Morse code is named after Samuel F.B. Morse who was the inventor and early developer of the system adopted for electrical telegraphy.

Each Morse code symbol is formed by a sequence of dits (.) and dahs (-). The dit duration can vary for signal clarity and operator skill, but for any one message, once established it is the basic unit of time measurement in Morse code. The duration of a dah is three times the duration of a dit. Each dit or dah within an encoded character is followed by a period of signal absence, called a space, equal to the dit duration [(Wikipedia)](https://en.wikipedia.org/wiki/Morse_code#).

## International Morse Code
This program uses the International Telecommunication Union (ITU) standard Morse code. Morse code was standardized by the International Telegraphy Congress and became the standard used by the ITU. More information on [Wikipedia](https://en.wikipedia.org/wiki/Morse_code#International_Morse_code) and [ITU](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf).

## Morse Code Alphabet
Here is the Morse code in letters, numbers, and punctuation. For more, see [Wikipedia](https://en.wikipedia.org/wiki/Morse_code#Letters,_numbers,_punctuation,_prosigns_for_Morse_code_and_non-Latin_variants). If there is a character that does not have a code, it will be replaced by a '#' sign.

**1. Letters**
| Letter | Code      | Letter | Code      | Letter | Code      |
| :---:  | :---:     | :---:  | :---:     | :---:  | :---:     |
| A      | .-        | J      | .---      | S      | ...       |
| B      | -...      | K      | -.-       | T      | -         |
| C      | -.-.      | L      | .-..      | U      | ..-       |
| D      | -..       | M      | --        | V      | ...-      |
| E      | .         | N      | -.        | W      | .--       |
| F      | ..-.      | O      | ---       | X      | -..-      |
| G      | --.       | P      | .--.      | Y      | -.--      |
| H      | ....      | Q      | --.-      | Z      | --..      |
| I      | ..        | R      | .-.       |        |           |

**2. Number**
| Number | Code      | Number | Code      | Number | Code      |
| :---:  | :---:     | :---:  | :---:     | :---:  | :---:     |
| 0      | -----     | 4      | ....-     | 8      | ---..     |
| 1      | .----     | 5      | .....     | 9      | ----.     |
| 2      | ..---     | 6      | -....     |        |           |
| 3      | ...--     | 7      | --...     |        | -         |

**3. Punctuation**
| Punctuation | Code      | Punctuation | Code      | Punctuation | Code      |
|    :---:    | :---:     |    :---:    | :---:     |    :---:    | :---:     |
| ;           | -.-.-.    | ,           | --..--    | :           | ---...    |
| -           | -....-    | !           | -.-.--    | +           | .-.-.     |
| $           | ...-..-   | )           | -.--.-    | "           | .-..-.    |
| ?           | ..--..    | .           | .-.-.-    | =           | -...-     |
| /           | -..-.     | '           | .----.    | _           | ..--.-    |
| &           | .-...     | (           | -.--.     | @           | .--.-.    |


## GUI Program
The GUI of this program uses Tkinter. To find out more about Tkinter, please visit [Tkinter Python](https://docs.python.org/3/library/tkinter.html#module-tkinter), [Tk Commands](https://tcl.tk/man/tcl8.6/TkCmd/contents.htm), [TKDocs](https://tkdocs.com/index.html), and [Python GUI Tkinter](https://www.geeksforgeeks.org/python-gui-tkinter/).

`screen = Tk()`: to initialize the tkinter and create the main window.

`screen.mainloop()`: an infinite loop used to run the application, wait for an event to occur, and process the event as long as the window is not closed.
```
Import tkinter
screen = Tk()
# widget code here
screen.mainloop()
```
`screen.config()`: to set configuration on screen such as background color, padding (x and y), width, height, etc.
`screen.title()`: set title on the screen.

## Widgets Used
The widgets used in this program are Text, Label, and Buttons.
`Text()`: display text in multiple lines
`Label()`: display boxes that can place text and images
`Buttons()`: display button on-screen and have command when the button’s clicked

## Others
1. This program uses the Pillow Library to resize the image. By using the `Image` and `ImageTk` class. Image class to resize image and ImageTk to display an image on the screen.
2. VLC used to play sound morse code and time module to give pause time
3. Pyperclip for copy text encoded code morse.

