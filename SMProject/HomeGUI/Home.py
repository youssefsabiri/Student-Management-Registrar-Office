
import subprocess
import pyttsx3
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"



def show_register_window():
    window.destroy()
    subprocess.run(['python', '../RegisterGUI/Register.py'])

def show_search_window():
    window.destroy()
    subprocess.run(['python', '../SearchGUI/Search.py'])

def show_delete_window():
    window.destroy()
    subprocess.run(['python', '../DeleteGUI/Delete.py'])

def show_display_window():
    window.destroy()
    subprocess.run(['python', '../DisplayGUI/Display.py'])



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x832")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    416.0,
    image=image_image_1
)

canvas.create_text(
    169.0,
    69.0,
    anchor="nw",
    text="WELCOME TO STUDENT MANAGEMENT SYSTEM",
    fill="#1E1E1E",
    font=("Inter", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_register_window(),
    relief="flat"
)
button_1.place(
    x=291.0,
    y=212.0,
    width=697.24365234375,
    height=58.257598876953125
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_search_window(),
    relief="flat"
)
button_2.place(
    x=291.0,
    y=326.0,
    width=697.24365234375,
    height=58.257598876953125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_delete_window(),
    relief="flat"
)
button_3.place(
    x=291.0,
    y=440.0,
    width=697.24365234375,
    height=58.257598876953125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_display_window(),
    relief="flat"
)
button_5.place(
    x=291.0,
    y=554.0,
    width=697.24365234375,
    height=58.257598876953125
)

window.resizable(False, False)

text_speech = pyttsx3.init()
voice = text_speech.getProperty('voices')  # get the available voices
text_speech.setProperty('voice', voice[1].id)
answer = "Welcome to student management app"

text_speech.say(answer)
text_speech.runAndWait()

window.mainloop()
