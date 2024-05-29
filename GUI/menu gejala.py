from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
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
    360.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    457.0,
    1280.0,
    782.0,
    fill="#09979D",
    outline="")

canvas.create_rectangle(
    384.0,
    33.0,
    853.0,
    672.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=423.0,
    y=434.0,
    width=392.0,
    height=47.0
)

canvas.create_rectangle(
    384.0,
    17.0,
    853.0,
    97.0,
    fill="#09979D",
    outline="")

canvas.create_text(
    428.0,
    33.0,
    anchor="nw",
    text="Apa Keluhan Anda?",
    fill="#FFFFFF",
    font=("Inter Bold", 40 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=423.0,
    y=212.0,
    width=392.0,
    height=47.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=423.0,
    y=286.0,
    width=392.0,
    height=47.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=423.0,
    y=508.0,
    width=392.0,
    height=47.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=423.0,
    y=582.0,
    width=392.0,
    height=47.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=423.0,
    y=360.0,
    width=392.0,
    height=47.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=423.0,
    y=143.0,
    width=392.0,
    height=47.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    106.0,
    72.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
