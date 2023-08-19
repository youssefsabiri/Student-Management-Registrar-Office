# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

import pyttsx3

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x832")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=832,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    416.0,
    image=image_image_1
)

canvas.create_text(
    71.0,
    56.0,
    anchor="nw",
    text="WELCOME TO STUDENT \nMANAGEMENT SYSTEM",
    fill="#1E1E1E",
    font=("Inter", 40 * -1)
)

canvas.create_rectangle(
    730.0,
    0.0,
    1280.0,
    832.0,
    fill="#DC9C61",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    983.0,
    359.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=836.0,
    y=347.0,
    width=294.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    983.0,
    499.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    show="*"  # For password hiding
)
entry_2.place(
    x=836.0,
    y=487.0,
    width=294.0,
    height=23.0
)

canvas.create_text(
    828.0,
    442.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Poppins Regular", 25 * -1)
)

canvas.create_text(
    828.0,
    302.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Poppins Regular", 25 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_credentials(),
    relief="flat"
)
button_1.place(
    x=768.0,
    y=582.0,
    width=459.24365234375,
    height=43.7293701171875
)

canvas.create_text(
    766.0,
    209.0,
    anchor="nw",
    text="Please Login:",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)


def show_new_window():
    subprocess.run(['python', '../HomeGUI/Home.py'])


def check_credentials():
    username = entry_1.get()
    password = entry_2.get()

    correct_username = "admin"  # Add your hardcoded username here
    correct_password = "password123"  # Add your hardcoded password here

    if username == correct_username and password == correct_password:
        text_speech = pyttsx3.init()
        voice = text_speech.getProperty('voices')  # get the available voices
        # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
        text_speech.setProperty('voice', voice[1].id)
        answer = "Login Successful!"
        text_speech.say(answer)
        text_speech.runAndWait()
        messagebox.showinfo("Success", "Login Successful!")
        window.destroy()  # This will close the login window
        show_new_window()  # Here you can add the code to show the new window
    else:
        text_speech = pyttsx3.init()
        voice = text_speech.getProperty('voices')  # get the available voices
        # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
        text_speech.setProperty('voice', voice[1].id)
        answer = lyrics = '''Have mercy on me, have mercy on my soul
Don't let my heart turn cold
Have mercy on me, have mercy on my soul
Don't let my heart turn cold
Have mercy on—
Many men
Many, many, many, many
Wish death upon me
Yeah, I don't cry no more
I don't look to the sky no more
Cause I got it on me
I got it on me
I got it on me
You can run up if you want'''

        messagebox.showerror("Error", "Invalid Credentials")
        text_speech.say(answer)
        text_speech.runAndWait()
        entry_1.delete(0, 'end')
        entry_2.delete(0, 'end')



window.resizable(False, False)
window.mainloop()