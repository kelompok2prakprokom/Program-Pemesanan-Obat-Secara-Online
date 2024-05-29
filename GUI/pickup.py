
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
    256.0,
    81.06157105211878,
    951.1007582640591,
    631.0805661191262,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    256.0,
    57.0,
    951.0,
    133.0,
    fill="#09979D",
    outline="")

canvas.create_text(
    533.0,
    71.0,
    anchor="nw",
    text="PICK UP",
    fill="#FFFFFF",
    font=("Inter Bold", 35 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    92.0,
    74.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_namapickup.png"))
entry_bg_1 = canvas.create_image(
    603.5,
    280.0,
    image=entry_image_1
)
entry_namapickup = Entry(
    bd=0,
    bg="#09979D",
    fg="#000716",
    highlightthickness=0
)
entry_namapickup.place(
    x=317.0,
    y=235.0,
    width=573.0,
    height=78.0
)

canvas.create_text(
    302.0,
    204.0,
    anchor="nw",
    text="Nama: ",
    fill="#09679D",
    font=("Kadwa Regular", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_nopickup.png"))
entry_bg_2 = canvas.create_image(
    603.5,
    431.0,
    image=entry_image_2
)
entry_nopickup = Entry(
    bd=0,
    bg="#09979D",
    fg="#000716",
    highlightthickness=0
)
entry_nopickup.place(
    x=317.0,
    y=385.0,
    width=573.0,
    height=78.0
)

canvas.create_text(
    302.0,
    355.0,
    anchor="nw",
    text="No. Telepon: ",
    fill="#09679D",
    font=("Kadwa Regular", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
