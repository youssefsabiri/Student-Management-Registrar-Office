# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import subprocess
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

import psycopg2

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"



def delete_student():
    connection = psycopg2.connect(
        dbname="test",
        user="postgres",
        password="mrrobot",
        host="localhost"
    )

    # Open a cursor to perform database operations
    c = connection.cursor()

    # Get the user input from the entries
    id_search = entry_1.get("1.0", "end-1c").strip()

    if id_search:
        try:
            user_id = int(id_search)
        except ValueError:
            messagebox.showerror("Error", "Invalid ID format")
            return

    # Create the SQL query
    query = "SELECT id FROM student WHERE id = %s"
    c.execute(query, (id_search,))

    result = c.fetchall()

    if len(result) == 0:
        messagebox.showinfo("Not Found", "No results found")
    else:
        # delete student
        query = "DELETE FROM student WHERE id = %s"
        c.execute(query, (id_search,))
        connection.commit()
        messagebox.showinfo("Success", "Student deleted successfully")
        show_new_window()


def show_new_window():
    window.destroy()
    subprocess.run(['python', '../HomeGUI/Home.py'])


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

canvas.create_rectangle(
    252.0,
    187.0,
    999.0,
    666.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    169.0,
    69.0,
    anchor="nw",
    text="WELCOME TO STUDENT MANAGEMENT SYSTEM",
    fill="#1E1E1E",
    font=("Inter", 40 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    613.0,
    428.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=466.0,
    y=416.0,
    width=294.0,
    height=23.0
)

canvas.create_text(
    460.0,
    374.0,
    anchor="nw",
    text="ID:",
    fill="#000000",
    font=("Poppins Regular", 25 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: delete_student(),
    relief="flat"
)
button_1.place(
    x=383.0,
    y=521.0,
    width=459.24365234375,
    height=43.7293701171875
)

canvas.create_text(
    343.0,
    251.0,
    anchor="nw",
    text="Type the ID of the student you want to delete:",
    fill="#000000",
    font=("Poppins Regular", 25 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_new_window(),
    relief="flat"
)
button_2.place(
    x=65.0,
    y=725.0,
    width=243.0,
    height=43.7293701171875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_3.place(
    x=965.0,
    y=725.0,
    width=243.0,
    height=43.7293701171875
)
window.resizable(False, False)
window.mainloop()