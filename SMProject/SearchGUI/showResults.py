from tkinter import ttk, Frame, Tk
import pandas as pd


def show_table(data, root):
    # create frame
    frame = Frame(root, width=1119, height=518, bg="white")
    frame.place(x=87, y=157)  # place the frame according to your layout

    # create Treeview with scrollbars
    table = ttk.Treeview(frame, height=10)  # Set the height to the number of rows you want visible
    table["show"] = "headings"  # Set the height to the number of rows you want visible
    table.place(relheight=1, relwidth=1)  # Make the table fill the frame

    # create scrollbars and assign the command to treeview yview and xview
    vsb = ttk.Scrollbar(frame, orient="vertical", command=table.yview)
    vsb.place(relx=0.981, rely=0.02, relheight=0.960)

    hsb = ttk.Scrollbar(frame, orient="horizontal", command=table.xview)
    hsb.place(relx=0.020, rely=0.981, relwidth=0.959)

    table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    table["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
    table.column("one", width=160)  # adjust the width to suit your needs
    table.column("two", width=160)
    table.column("three", width=160)
    table.column("four", width=160)
    table.column("five", width=160)
    table.column("six", width=160)
    table.column("seven", width=160)

    table.heading("one", text="ID")
    table.heading("two", text="First Name")
    table.heading("three", text="Last Name")
    table.heading("four", text="Birth Date")
    table.heading("five", text="Email")
    table.heading("six", text="Phone Number")
    table.heading("seven", text="Country")

    # Inserting the data
    # Inserting the data
    for _, row in data.iterrows():
        row = list(row)
        row[3] = row[3].strftime('%Y-%m-%d')  # formatting date
        table.insert('', 'end', values=[str(e) for e in row])