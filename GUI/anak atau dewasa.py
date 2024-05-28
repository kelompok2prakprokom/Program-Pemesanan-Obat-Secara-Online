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
    332.0,
    113.0,
    908.0,
    537.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    332.0,
    103.0,
    908.0,
    183.0,
    fill="#09979D",
    outline="")

canvas.create_text(
    510.0,
    119.0,
    anchor="nw",
    text="Obat untuk",
    fill="#FFFFFF",
    font=("Inter Bold", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=384.0,
    y=360.0,
    width=471.0,
    height=63.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    106.0,
    72.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=384.0,
    y=240.0,
    width=471.0,
    height=63.0
)
window.resizable(False, False)
window.mainloop()
