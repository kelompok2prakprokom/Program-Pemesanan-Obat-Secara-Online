from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# Define the base path using __file__
BASE_PATH = Path(__file__).resolve().parent

# Define the assets path relative to the base path
ASSETS_PATH = BASE_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_file_exists(file_path):
    if not file_path.exists():
        print(f"Error: The file {file_path} does not exist.")
        return False
    return True

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

image_path_1 = relative_to_assets("image_1.png")
if check_file_exists(image_path_1):
    image_image_1 = PhotoImage(file=image_path_1)
    image_1 = canvas.create_image(640.0, 360.0, image=image_image_1)

canvas.create_rectangle(
    0.0,
    457.0,
    1280.0,
    782.0,
    fill="#09979D",
    outline="")

canvas.create_rectangle(
    126.0,
    54.0,
    1153.0,
    644.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    332.0,
    16.0,
    908.0,
    96.0,
    fill="#09979D",
    outline="")

canvas.create_text(
    543.0,
    33.0,
    anchor="nw",
    text="PUSING",
    fill="#FFFFFF",
    font=("Inter Bold", 40 * -1)
)

button_image_1 = relative_to_assets("button_11.png")
if check_file_exists(button_image_1):
    button_image_1 = PhotoImage(file=button_image_1)
    button_11 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    button_11.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

button_image_2 = relative_to_assets("button_12.png")
if check_file_exists(button_image_2):
    button_image_2 = PhotoImage(file=button_image_2)
    button_12 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    button_12.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

image_path_2 = relative_to_assets("image_2.png")
if check_file_exists(image_path_2):
    image_image_2 = PhotoImage(file=image_path_2)
    image_2 = canvas.create_image(92.0, 74.0, image=image_image_2)

window.resizable(False, False)
window.mainloop()
