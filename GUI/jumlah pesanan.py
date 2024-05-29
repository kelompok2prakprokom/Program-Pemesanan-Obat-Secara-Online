
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


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
    331.0,
    71.0,
    anchor="nw",
    text="MASUKKAN JUMLAH PESANAN",
    fill="#FFFFFF",
    font=("Inter Bold", 35 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_angka1.png"))
button_angka1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_angka1 clicked"),
    relief="flat"
)
button_angka1.place(
    x=489.0,
    y=158.0,
    width=229.0,
    height=58.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_angka2.png"))
button_angka2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_angka2 clicked"),
    relief="flat"
)
button_angka2.place(
    x=489.0,
    y=256.0,
    width=229.0,
    height=58.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_angka3.png"))
button_angka3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_angka3 clicked"),
    relief="flat"
)
button_angka3.place(
    x=490.0,
    y=354.0,
    width=229.0,
    height=58.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_angka4.png"))
button_angka4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_angka4 clicked"),
    relief="flat"
)
button_angka4.place(
    x=489.0,
    y=452.0,
    width=229.0,
    height=58.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_angka5.png"))
button_angka5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_angka5 clicked"),
    relief="flat"
)
button_angka5.place(
    x=489.0,
    y=550.0,
    width=229.0,
    height=58.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    92.0,
    74.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()