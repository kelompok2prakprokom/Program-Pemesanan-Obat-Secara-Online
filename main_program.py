from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import json
from datetime import datetime
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"gambar")
with open('obat.json', 'r') as file:
    obat = json.load(file)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_file_exists(file_path):
    if not file_path.exists():
        print(f"Error: The file {file_path} does not exist.")
        return False
    return True

def loginAccount():
    global login
    login=Tk()
    login.title('Login')
    login.geometry('925x500+300+200')
    login.configure(bg="#fff")
    login.resizable (False, False)

    image = Image.open('gambar/logo apotek.jpg')
    image = image.resize((400, 400), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(image) 
    label = Label(login, image=img)
    label.pack()
    label.place(x=50,y=50)

    frame=Frame(login, width=350,height= 350, bg="white") 
    frame.place(x=480,y=70)

    heading = Label(frame, text='Sign in', fg='#00CED1', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold')) 
    heading.place(x=100,y=5)

    #------------------------------------------------------------------------------------------------------------
    def auth_account():
        global name
        name=str(user.get())
        pw=str(code.get())
        with open('data.akun.json', 'r') as file:
            data_akun = json.load(file)
        for i in range(0, len(data_akun["akun"])):
            if name == data_akun["akun"][i]["Username"] and pw == data_akun["akun"][i]["Password"]:
                login.destroy()
                menu_utama()
                break
        else:
            messagebox.showerror("Login Gagal!", "Username atau Password salah!")
    def on_enter(e):
        user.delete(0, 'end')
    def on_leave(e):
        name=str(user.get())
        if name=='' :
            user.insert(0, 'Username')
    user = Entry(frame, width=35,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11)) 
    user.place(x=30,y=80) 
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter) 
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25,y=107) 
    #------------------------------------------------------------------------------------------------------------
    def on_enter(e):
        code.delete(0, 'end')
        code.configure(show="*")
    def on_leave(e):
        pw=code.get()
        code.configure(show="*")
        if pw == '' :
            code.insert(0, 'Password')
    code = Entry(frame, width=25,fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11)) 
    code.place(x=30,y=150) 
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter) 
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25,y=177) 
    #############################################################################################################
    Button (frame, width=39, pady=7, text='Sign in', bg='#00CED1',fg='white', border='0', command=auth_account).place(x=35,y=204) 

    label=Label(frame, text="Don't have an account?", fg='black', bg='white', font= ('Microsoft Vanei UI Light',9))
    label.place(x=75,y=270)

    sign_up= Button(frame,width=6,text='Sign Up', border=0, bg='white',cursor='hand2',fg='#00CED1', command=signInToSignUp )
    sign_up.place(x=215,y=270)

    login.mainloop()

def signInToSignUp():
    login.destroy()
    open_signup()
def signUpToSignIn():
    signup_window.destroy()
    open_signup()

def open_signup():
    global signup_window
    def registerAccount():
            with open('data.akun.json', 'r') as file:
                data_akun = json.load(file)
            Username = str(signup_user.get())
            Password = str(signup_code.get())
            confirm_pw = confirm_code.get()
            if Username == "Username" and Password == "Password" and confirm_pw == "Confirm Password":
                messagebox.showerror("Failed", "Harap diisi terlebih dahulu")
            elif Username == "Username":
                messagebox.showerror("Failed", "Username harus diisi!")
            elif Password == confirm_pw:
                for i in range(0, len(data_akun["akun"])):
                    if Username == data_akun["akun"][i]["Username"]:
                        messagebox.showerror("Error!", "Username yang ada pilih sudah digunakan!")
                        break
                else:
                    # with open("purchase.history.json", 'r') as file:
                    #     data = json.loads(file.read()) 
                    # data[Username] = []
                    # with open("purchase.history.json", 'w') as file:
                    #     file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
                    y = {}
                    y.update({"Username": Username})
                    y.update({"Password": Password})
                    Addjson(y)
            else:
                messagebox.showerror("Failed", "Password yang Anda masukkan berbeda!")

    def Addjson(new_data, filename='data.akun.json'):
            with open(filename,'r+') as file:
                file_data = json.load(file)
                file_data["akun"].append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
            messagebox.showinfo("Success", "Akun berhasil dibuat!")
            signup_window.destroy()
            menu_utama()
            
    signup_window = Tk()
    signup_window.title('Sign Up')
    signup_window.geometry('925x500+300+200')
    signup_window.configure(bg="white")
    signup_window.resizable(False, False)
        
    signup_image = Image.open('gambar/logo apotek.jpg')  
    signup_image = signup_image.resize((400, 400), Image.Resampling.LANCZOS)
    signup_img = ImageTk.PhotoImage(signup_image)
    signup_label = Label(signup_window, image=signup_img)
    signup_label.image = signup_img 
    signup_label.pack()
    signup_label.place(x=50, y=50)
        
    frame_signup = Frame(signup_window, width=350, height=350, bg="white")
    frame_signup.place(x=480, y=70)
        
    heading_signup = Label(frame_signup, text='Sign Up', fg='#00CED1', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading_signup.place(x=100, y=5)

        # Sign up username entry
    def on_enter(e):
        signup_user.delete(0, 'end')
    def on_leave(e):
        name = signup_user.get()
        if name == '':
            signup_user.insert(0, 'Username')
    signup_user = Entry(frame_signup, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    signup_user.place(x=30, y=80)
    signup_user.insert(0, 'Username')
    signup_user.bind('<FocusIn>', on_enter)
    signup_user.bind('<FocusOut>', on_leave)
    Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=107)

        # Sign up password entry
    def on_enter(e):
        signup_code.delete(0, 'end')
    def on_leave(e):
        name = signup_code.get()
        if name == '':
            signup_code.insert(0, 'Password')
    signup_code = Entry(frame_signup, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    signup_code.place(x=30, y=150)
    signup_code.insert(0, 'Password')
    signup_code.bind('<FocusIn>', on_enter)
    signup_code.bind('<FocusOut>', on_leave)
    Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=177)

        # Confirm password entry
    def on_enter(e):
        confirm_code.delete(0, 'end')
    def on_leave(e):
        name = confirm_code.get()
        if name == '':
            confirm_code.insert(0, 'Confirm Password')
    confirm_code = Entry(frame_signup, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)
    Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=247)

        # Sign up button
    Button(frame_signup, width=39, pady=7, text='Create Account', bg='#00CED1', fg='white', border='0', command=registerAccount).place(x=35, y=280)
    
    signup_window.mainloop()
        
def menu_utama():
    global main
    global totalHarga
    global namaObat
    global jumlahPesanObat
    global hargaObat
    totalHarga = []
    namaObat = []
    hargaObat = []
    jumlahPesanObat = []
    def pusing():
        main.withdraw()
        cekUsiaPusing()
    def diare():
        main.withdraw()
        cekUsiaDiare()
    def demam():
        main.withdraw()
        cekUsiaDemam()
    def batuk():
        main.withdraw()
        cekUsiaBatuk()
    def flu():
        main.withdraw()
        cekUsiaFlu()
    def radang():
        main.withdraw()
        cekUsiaRadang()
    def pilek():
        main.withdraw()
        cekUsiaPilek()
    

    main = Tk()
    main.title("Menu Utama")
    main.geometry("1280x720")
    main.configure(bg="#FFFFFF")

    canvas = Canvas(
        main,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    # Load image_1.png if it exists
    image_path_1 = relative_to_assets("image_1.png")
    if check_file_exists(image_path_1):
        image_image_1 = PhotoImage(file=image_path_1)
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
        outline=""
    )

    canvas.create_rectangle(
        384.0,
        33.0,
        853.0,
        672.0,
        fill="#FFFFFF",
        outline=""
    )


    # Load button_1.png if it exists
    button_path_19 = relative_to_assets("button_19.png")
    if check_file_exists(button_path_19):
        button_image_19 = PhotoImage(file=button_path_19)
        button_19 = Button(
            image=button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=pusing,
            relief="flat"
        )
        button_19.place(
            x=423.0,
            y=143.0,
            width=392.0,
            height=47.0
        )
    button_path_1 = relative_to_assets("button_13.png")
    if check_file_exists(button_path_1):
        button_image_1 = PhotoImage(file=button_path_1)
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=diare,
            relief="flat"
        )
        button_1.place(
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
        outline=""
    )

    canvas.create_text(
        428.0,
        33.0,
        anchor="nw",
        text="Apa Keluhan Anda?",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )

    # Load button_2.png if it exists
    button_path_2 = relative_to_assets("button_14.png")
    if check_file_exists(button_path_2):
        button_image_2 = PhotoImage(file=button_path_2)
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=demam,
            relief="flat"
        )
        button_2.place(
            x=423.0,
            y=212.0,
            width=392.0,
            height=47.0
        )

    # Load button_3.png if it exists
    button_path_3 = relative_to_assets("button_15.png")
    if check_file_exists(button_path_3):
        button_image_3 = PhotoImage(file=button_path_3)
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=batuk,
            relief="flat"
        )
        button_3.place(
            x=423.0,
            y=286.0,
            width=392.0,
            height=47.0
        )

    # Load button_4.png if it exists
    button_path_4 = relative_to_assets("button_16.png")
    if check_file_exists(button_path_4):
        button_image_4 = PhotoImage(file=button_path_4)
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=flu,
            relief="flat"
        )
        button_4.place(
            x=423.0,
            y=508.0,
            width=392.0,
            height=47.0
        )

    # Load button_5.png if it exists
    button_path_5 = relative_to_assets("button_17.png")
    if check_file_exists(button_path_5):
        button_image_5 = PhotoImage(file=button_path_5)
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=radang,
            relief="flat"
        )
        button_5.place(
            x=423.0,
            y=582.0,
            width=392.0,
            height=47.0
        )

    # Load button_6.png if it exists
    button_path_6 = relative_to_assets("button_18.png")
    if check_file_exists(button_path_6):
        button_image_6 = PhotoImage(file=button_path_6)
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=pilek,
            relief="flat"
        )
        button_6.place(
            x=423.0,
            y=360.0,
            width=392.0,
            height=47.0
        )
    button_image_8 = PhotoImage(
        file=relative_to_assets("button_order.png"))
    button_order = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=mainToAmbil,
        relief="flat"
    )
    button_order.place(
        x=1024.0,
        y=568.0,
        width=145.0,
        height=60.0
    )
    # Load image_2.png if it exists
    image_path_2 = relative_to_assets("image_2.png")
    if check_file_exists(image_path_2):
        image_image_2 = PhotoImage(file=image_path_2)
        image_2 = canvas.create_image(
            106.0,
            72.0,
            image=image_image_2
        )

    main.resizable(False, False)
    main.mainloop()

def cekPusingToMain():
    usia_pusing.destroy()
    main.deiconify()
def cekDiareToMain():
    usia_diare.destroy()
    main.deiconify()
def cekDemamToMain():
    usia_demam.destroy()
    main.deiconify()
def cekBatukToMain():
    usia_batuk.destroy()
    main.deiconify()
def cekFluToMain():
    usia_flu.destroy()
    main.deiconify()
def cekRadangToMain():
    usia_radang.destroy()
    main.deiconify()
def cekPilekToMain():
    usia_pilek.destroy()
    main.deiconify()

def cekUsiaPusing():
    global usia_pusing
    def pusing():
        if cekAnak == True:
            pusingAnak()
        elif cekDewasa == True:
            pusingDewasa()
        else:
            print("error!")
    
    def anak():
        global cekDewasa
        global cekAnak
        global pusing_dewasa
        pusing_dewasa = False
        cekAnak = True
        cekDewasa = False
        usia_pusing.destroy()
        pusing()

    def dewasa():
        global cekDewasa
        global cekAnak
        global pusing_anak
        pusing_anak = False
        cekDewasa = True
        cekAnak = False
        usia_pusing.destroy()
        pusing()
        
    usia_pusing = Toplevel()
    usia_pusing.title("Pemilihan Obat")
    usia_pusing.geometry("1280x720")
    usia_pusing.configure(bg = "#FFFFFF")

    canvas = Canvas(
        usia_pusing,
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
    button_back = PhotoImage(
        file=relative_to_assets("button_back.png"))
    button_back_1 = Button(
        usia_pusing,
        image=button_back,
        borderwidth=0,
        highlightthickness=0,
        command=cekPusingToMain,
        relief="flat"
    )
    button_back_1.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )

    button_8 = Image.open("gambar/button_8.png")
    button_8_img = ImageTk.PhotoImage(button_8)
    button_8 = Button(usia_pusing,
        image=button_8_img,
        borderwidth=0,
        highlightthickness=0,
        command=dewasa,
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
    button_9 = Button(usia_pusing,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=anak,
        relief="flat"
    )
    button_9.place(
        x=384.0,
        y=240.0,
        width=471.0,
        height=63.0
    )
    usia_pusing.resizable(False, False)
    usia_pusing.mainloop()

def cekUsiaDiare():
    global usia_diare
    def diare():
        if cekAnak == True:
            diareAnak()
        elif cekDewasa == True:
            diareDewasa()
        else:
            print("error!")
    
    def anak():
        global cekDewasa
        global cekAnak
        global diare_dewasa
        cekAnak = True
        cekDewasa = False
        diare_dewasa = False
        usia_diare.destroy()
        diare()

    def dewasa():
        global cekDewasa
        global cekAnak
        global diare_anak
        diare_anak = False
        cekDewasa = True
        cekAnak = False
        usia_diare.destroy()
        diare()
        
    usia_diare = Toplevel()
    usia_diare.title("Pemilihan Obat")
    usia_diare.geometry("1280x720")
    usia_diare.configure(bg = "#FFFFFF")

    canvas = Canvas(
        usia_diare,
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
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        usia_diare,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=cekDiareToMain,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_8 = Image.open("gambar/button_8.png")
    button_8_img = ImageTk.PhotoImage(button_8)
    button_8 = Button(usia_diare,
        image=button_8_img,
        borderwidth=0,
        highlightthickness=0,
        command=dewasa,
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
    button_9 = Button(usia_diare,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=anak,
        relief="flat"
    )
    button_9.place(
        x=384.0,
        y=240.0,
        width=471.0,
        height=63.0
    )
    usia_diare.resizable(False, False)
    usia_diare.mainloop()

def cekUsiaDemam():
    global usia_demam
    def demam():
        if cekAnak == True:
            demamAnak()
        elif cekDewasa == True:
            demamDewasa()
        else:
            print("error!")
    
    def anak():
        global cekDewasa
        global cekAnak
        
        cekAnak = True
        cekDewasa = False
        usia_demam.destroy()
        demam()

    def dewasa():
        global cekDewasa
        global cekAnak
        
        cekDewasa = True
        cekAnak = False
        usia_demam.destroy()
        demam()
        
    usia_demam = Toplevel()
    usia_demam.title("Pemilihan Obat")
    usia_demam.geometry("1280x720")
    usia_demam.configure(bg = "#FFFFFF")

    canvas = Canvas(
        usia_demam,
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
    button_back = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back_1 = Button(
        usia_demam,
        image=button_back,
        borderwidth=0,
        highlightthickness=0,
        command=cekDemamToMain,
        relief="flat"
    )
    button_back_1.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_8 = Image.open("gambar/button_8.png")
    button_8_img = ImageTk.PhotoImage(button_8)
    button_8 = Button(usia_demam,
        image=button_8_img,
        borderwidth=0,
        highlightthickness=0,
        command=dewasa,
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
    button_9 = Button(usia_demam,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=anak,
        relief="flat"
    )
    button_9.place(
        x=384.0,
        y=240.0,
        width=471.0,
        height=63.0
    )
    usia_demam.resizable(False, False)
    usia_demam.mainloop()

def cekUsiaBatuk():
    global usia_batuk
    def batuk():
        if cekAnak == True:
            batukAnak()
        elif cekDewasa == True:
            batukDewasa()
        else:
            print("error!")
    
    def anak():
        global cekDewasa
        global cekAnak
        global batuk_dewasa
        batuk_dewasa = False
        cekAnak = True
        cekDewasa = False
        usia_batuk.destroy()
        batuk()

    def dewasa():
        global cekDewasa
        global cekAnak
        global batuk_anak
        batuk_anak = False
        cekDewasa = True
        cekAnak = False
        usia_batuk.destroy()
        batuk()
        
    usia_batuk = Toplevel()
    usia_batuk.title("Pemilihan Obat")
    usia_batuk.geometry("1280x720")
    usia_batuk.configure(bg = "#FFFFFF")

    canvas = Canvas(
        usia_batuk,
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
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        usia_batuk,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=cekBatukToMain,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_8 = Image.open("gambar/button_8.png")
    button_8_img = ImageTk.PhotoImage(button_8)
    button_8 = Button(usia_batuk,
        image=button_8_img,
        borderwidth=0,
        highlightthickness=0,
        command=dewasa,
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
    button_9 = Button(usia_batuk,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=anak,
        relief="flat"
    )
    button_9.place(
        x=384.0,
        y=240.0,
        width=471.0,
        height=63.0
    )
    usia_batuk.resizable(False, False)
    usia_batuk.mainloop()

def cekUsiaFlu():
    global usia_flu
    def flu():
        if cekAnak == True:
            fluAnak()
        elif cekDewasa == True:
            fluDewasa()
        else:
            print("error!")
    
    def anak():
        global cekDewasa
        global cekAnak
        global flu_dewasa
        flu_dewasa = False
        cekAnak = True
        cekDewasa = False
        usia_flu.destroy()
        flu()

    def dewasa():
        global cekDewasa
        global cekAnak
        global flu_anak
        flu_anak = False
        cekDewasa = True
        cekAnak = False
        usia_flu.destroy()
        flu()
        
    usia_flu = Toplevel()
    usia_flu.title("Pemilihan Obat")
    usia_flu.geometry("1280x720")
    usia_flu.configure(bg = "#FFFFFF")

    canvas = Canvas(
        usia_flu,
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
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        usia_flu,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=cekFluToMain,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_8 = Image.open("gambar/button_8.png")
    button_8_img = ImageTk.PhotoImage(button_8)
    button_8 = Button(usia_flu,
        image=button_8_img,
        borderwidth=0,
        highlightthickness=0,
        command=dewasa,
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
    button_9 = Button(usia_flu,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=anak,
        relief="flat"
    )
    button_9.place(
        x=384.0,
        y=240.0,
        width=471.0,
        height=63.0
    )
    usia_flu.resizable(False, False)
    usia_flu.mainloop()

def cekUsiaRadang():
    global usia_radang
    def radang():
        if cekAnak == True:
            radangAnak()
        elif cekDewasa == True:
            radangDewasa()
        else:
            print("error!")
    
    def anak():
        global cekDewasa
        global cekAnak
        global radang_dewasa
        radang_dewasa = False
        cekAnak = True
        cekDewasa = False
        usia_radang.destroy()
        radang()

    def dewasa():
        global cekDewasa
        global cekAnak
        global radang_anak
        radang_anak = False
        cekDewasa = True
        cekAnak = False
        usia_radang.destroy()
        radang()
        
    usia_radang = Toplevel()
    usia_radang.title("Pemilihan Obat")
    usia_radang.geometry("1280x720")
    usia_radang.configure(bg = "#FFFFFF")

    canvas = Canvas(
        usia_radang,
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
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        usia_radang,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=cekRadangToMain,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_8 = Image.open("gambar/button_8.png")
    button_8_img = ImageTk.PhotoImage(button_8)
    button_8 = Button(usia_radang,
        image=button_8_img,
        borderwidth=0,
        highlightthickness=0,
        command=dewasa,
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
    button_9 = Button(usia_radang,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=anak,
        relief="flat"
    )
    button_9.place(
        x=384.0,
        y=240.0,
        width=471.0,
        height=63.0
    )
    usia_radang.resizable(False, False)
    usia_radang.mainloop()

def cekUsiaPilek():
    global usia_pilek
    def pilek():
        if cekAnak == True:
            pilekAnak()
        elif cekDewasa == True:
            pilekDewasa()
        else:
            print("error!")
    
    def anak():
        global cekDewasa
        global cekAnak
        global pilek_dewasa
        pilek_dewasa = False
        cekAnak = True
        cekDewasa = False
        usia_pilek.destroy()
        pilek()

    def dewasa():
        global cekDewasa
        global cekAnak
        global pilek_anak
        pilek_anak = False
        cekDewasa = True
        cekAnak = False
        usia_pilek.destroy()
        pilek()
        
    usia_pilek = Toplevel()
    usia_pilek.title("Pemilihan Obat")
    usia_pilek.geometry("1280x720")
    usia_pilek.configure(bg = "#FFFFFF")

    canvas = Canvas(
        usia_pilek,
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
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        usia_pilek,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=cekPilekToMain,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_8 = Image.open("gambar/button_8.png")
    button_8_img = ImageTk.PhotoImage(button_8)
    button_8 = Button(usia_pilek,
        image=button_8_img,
        borderwidth=0,
        highlightthickness=0,
        command=dewasa,
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
    button_9 = Button(usia_pilek,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=anak,
        relief="flat"
    )
    button_9.place(
        x=384.0,
        y=240.0,
        width=471.0,
        height=63.0
    )
    usia_pilek.resizable(False, False)
    usia_pilek.mainloop()

def pusingToPilih():
    if (pusing_anak):
        pusing_anak.destroy()
        cekUsiaPusing()
    else:
        pusing_dewasa.destroy()
        cekUsiaPusing()
def diareToPilih():
    if (diare_anak):
        diare_anak.destroy()
        cekUsiaDiare()
    else:
        diare_dewasa.destroy()
        cekUsiaDiare()
def demamToPilih():
    if (cekAnak):
        demam_anak.destroy()
        cekUsiaDemam()
    else:
        demam_dewasa.destroy()
        cekUsiaDemam()
def batukToPilih():
    if (batuk_anak):
        batuk_anak.destroy()
        cekUsiaBatuk()
    else:
        batuk_dewasa.destroy()
        cekUsiaBatuk()
def fluToPilih():
    if (flu_anak):
        flu_anak.destroy()
        cekUsiaFlu()
    else:
        flu_dewasa.destroy()
        cekUsiaFlu()
def radangToPilih():
    if (radang_anak):
        radang_anak.destroy()
        cekUsiaRadang()
    else:
        radang_dewasa.destroy()
        cekUsiaRadang()
def pilekToPilih():
    if (pilek_anak):
        pilek_anak.destroy()
        cekUsiaPilek()
    else:
        pilek_dewasa.destroy()
        cekUsiaPilek()

def jumlahToPusing():
    if pusing_anak:
        jumlah.destroy()
        pusingAnak()
    elif pusing_dewasa:
        jumlah.destroy()
        pusingDewasa()
def jumlahToDiare():
    if diare_anak:
        jumlah.destroy()
        diareAnak()
    elif diare_dewasa:
        jumlah.destroy()
        diareDewasa()
def jumlahToDemam():
    if demam_anak:
        jumlah.destroy()
        demamAnak()
    elif demam_dewasa:
        jumlah.destroy()
        demamDewasa()
def jumlahToBatuk():
    if batuk_anak:
        jumlah.destroy()
        batukAnak()
    elif batuk_dewasa:
        jumlah.destroy()
        batukDewasa()
def jumlahToFlu():
    if flu_anak:
        jumlah.destroy()
        fluAnak()
    elif flu_dewasa:
        jumlah.destroy()
        fluDewasa()
def jumlahToRadang():
    if radang_anak:
        jumlah.destroy()
        radangAnak()
    elif radang_dewasa:
        jumlah.destroy()
        radangDewasa()
def jumlahToPilek():
    if pilek_anak:
        jumlah.destroy()
        pilekAnak()
    elif pilek_dewasa:
        jumlah.destroy()
        pilekDewasa()
        
        
def pusingAnak():
    global pusing_anak
    def jumlahPesanan1():
        global jumlah
        pusing_anak.destroy()
        nama_obat = "Paracetamol (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Pusing"]["Paracetamol (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPusing,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        pusing_anak.destroy()
        nama_obat = "Ibuprofen (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Pusing"]["Ibuprofen (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPusing,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()        
    
    pusing_anak = Toplevel()
    pusing_anak.geometry("1280x720")
    pusing_anak.configure(bg = "#FFFFFF")


    canvas = Canvas(
        pusing_anak,
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
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        pusing_anak,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=pusingToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_31.png"))
    button_31 = Button(
        pusing_anak,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_31.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_32.png"))
    button_32 = Button(
        pusing_anak,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_32.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    pusing_anak.resizable(False, False)
    pusing_anak.mainloop()

def pusingDewasa():
    global pusing_dewasa
    def jumlahPesanan1():
        global jumlah
        pusing_dewasa.destroy()
        nama_obat = "Paracetamol"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Pusing"]["Paracetamol"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPusing,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        pusing_dewasa.destroy()
        nama_obat = "Bodrex"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Pusing"]["Bodrex"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPusing,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
    
    pusing_dewasa = Toplevel()
    pusing_dewasa.geometry("1280x720")
    pusing_dewasa.configure(bg = "#FFFFFF")

    canvas = Canvas(
        pusing_dewasa,
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

    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        pusing_dewasa,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=pusingToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = relative_to_assets("button_11.png")
    if check_file_exists(button_image_1):
        button_image_1 = PhotoImage(file=button_image_1)
        button_11 = Button(
            pusing_dewasa,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahPesanan1,
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
            pusing_dewasa,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahPesanan2,
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

    pusing_dewasa.resizable(False, False)
    pusing_dewasa.mainloop()

def diareAnak():
    global diare_anak
    def jumlahPesanan1():
        global jumlah
        diare_anak.destroy()
        nama_obat = "zinc (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Diare"]["zinc (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDiare,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        diare_anak.destroy()
        nama_obat = "Oralit (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Diare"]["Oralit (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDiare,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
      
    diare_anak = Toplevel()
    diare_anak.geometry("1280x720")
    diare_anak.configure(bg = "#FFFFFF")


    canvas = Canvas(
        diare_anak,
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
        559.0,
        33.0,
        anchor="nw",
        text="DIARE",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        diare_anak,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=diareToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_39.png"))
    button_39 = Button(
        diare_anak,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_39.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_40.png"))
    button_40 = Button(
        diare_anak,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_40.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    diare_anak.resizable(False, False)
    diare_anak.mainloop()

def diareDewasa():
    global diare_dewasa
    def jumlahPesanan1():
        global jumlah
        diare_dewasa.destroy()
        nama_obat = "Oralit"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Diare"]["Oralit"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDiare,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        diare_dewasa.destroy()
        nama_obat = "Entrostop"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Diare"]["Entrostop"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDiare,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()


    
    diare_dewasa = Toplevel()
    diare_dewasa.geometry("1280x720")
    diare_dewasa.configure(bg = "#FFFFFF")


    canvas = Canvas(
        diare_dewasa,
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
        559.0,
        33.0,
        anchor="nw",
        text="DIARE",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        diare_dewasa,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=diareToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_21.png"))
    button_21 = Button(
        diare_dewasa,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_21.place(
        x=170.0,
        y=374.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_22.png"))
    button_22 = Button(
        diare_dewasa,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_22.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    diare_dewasa.resizable(False, False)
    diare_dewasa.mainloop()

def demamAnak():
    global demam_anak
    def jumlahPesanan1():
        global jumlah
        demam_anak.destroy()
        nama_obat = "Paracetamol (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Demam"]["Paracetamol (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDemam,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        demam_anak.destroy()
        nama_obat = "Ibuprofen (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Demam"]["Ibuprofen (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDemam,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()

    
    demam_anak = Toplevel()
    demam_anak.geometry("1280x720")
    demam_anak.configure(bg = "#FFFFFF")


    canvas = Canvas(
        demam_anak,
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
        541.0,
        33.0,
        anchor="nw",
        text="DEMAM",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        demam_anak,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=demamToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_33.png"))
    button_33 = Button(
        demam_anak,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_33.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_34.png"))
    button_34 = Button(
        demam_anak,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_34.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    demam_anak.resizable(False, False)
    demam_anak.mainloop()

def demamDewasa():
    global demam_dewasa
    def jumlahPesanan1():
        global jumlah
        demam_dewasa.destroy()
        nama_obat = "Paracetamol"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Demam"]["Paracetamol"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDemam,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        demam_dewasa.destroy()
        nama_obat = "Ibuprofen"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Demam"]["Ibuprofen"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToDemam,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()

    demam_dewasa = Toplevel()
    demam_dewasa.geometry("1280x720")
    demam_dewasa.configure(bg = "#FFFFFF")


    canvas = Canvas(
        demam_dewasa,
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
        541.0,
        33.0,
        anchor="nw",
        text="DEMAM",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        demam_dewasa,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=demamToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        demam_dewasa,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_10.place(
        x=170.0,
        y=374.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_20.png"))
    button_20 = Button(
        demam_dewasa,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_20.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    demam_dewasa.resizable(False, False)
    demam_dewasa.mainloop()
    
def batukAnak():
    global batuk_anak
    def jumlahPesanan1():
        global jumlah
        
        batuk_anak.destroy()
        nama_obat = "Hufagrip (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Batuk"]["Hufagrip (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToBatuk,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        batuk_anak.destroy()
        nama_obat = "OBH Combi (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Batuk"]["OBH Combi (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToBatuk,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()

    
    batuk_anak = Toplevel()
    batuk_anak.geometry("1280x720")
    batuk_anak.configure(bg = "#FFFFFF")


    canvas = Canvas(
        batuk_anak,
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
        551.0,
        33.0,
        anchor="nw",
        text="BATUK",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        batuk_anak,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=batukToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_35.png"))
    button_35 = Button(
        batuk_anak,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_35.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_36.png"))
    button_36 = Button(
        batuk_anak,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_36.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    batuk_anak.resizable(False, False)
    batuk_anak.mainloop()
    
def batukDewasa():
    global batuk_dewasa
    def jumlahPesanan1():
        global jumlah
        
        batuk_dewasa.destroy()
        nama_obat = "OBH Combi"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Batuk"]["OBH Combi"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToBatuk,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        batuk_dewasa.destroy()
        nama_obat = "Siladex"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Batuk"]["Siladex"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToBatuk,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
    
    batuk_dewasa = Toplevel()
    batuk_dewasa.geometry("1280x720")
    batuk_dewasa.configure(bg = "#FFFFFF")


    canvas = Canvas(
        batuk_dewasa,
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
        551.0,
        33.0,
        anchor="nw",
        text="BATUK",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        batuk_dewasa,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=batukToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_23.png"))
    button_23 = Button(
        batuk_dewasa,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_23.place(
        x=170.0,
        y=374.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_24.png"))
    button_24 = Button(
        batuk_dewasa,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_24.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    batuk_dewasa.resizable(False, False)
    batuk_dewasa.mainloop()

def fluAnak():
    global flu_anak
    def jumlahPesanan1():
        global jumlah
        
        flu_anak.destroy()
        nama_obat = "Tempra (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Flu"]["Tempra (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToFlu,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        flu_anak.destroy()
        nama_obat = "OBH Junior (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Flu"]["OBH Junior (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToFlu,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()


    flu_anak = Toplevel()
    flu_anak.geometry("1280x720")
    flu_anak.configure(bg = "#FFFFFF")


    canvas = Canvas(
        flu_anak,
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
        581.0,
        33.0,
        anchor="nw",
        text="FLU",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        flu_anak,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=fluToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_41.png"))
    button_41 = Button(
        flu_anak,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_41.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_42.png"))
    button_42 = Button(
        flu_anak,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_42.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    flu_anak.resizable(False, False)
    flu_anak.mainloop()

def fluDewasa():
    global flu_dewasa
    def jumlahPesanan1():
        global jumlah
        
        flu_dewasa.destroy()
        nama_obat = "Neozep forte"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Flu"]["Neozep forte"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToFlu,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        flu_dewasa.destroy()
        nama_obat = "Mixagrip flu"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Flu"]["Mixagrip flu"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToFlu,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
 
    flu_dewasa = Toplevel()
    flu_dewasa.geometry("1280x720")
    flu_dewasa.configure(bg = "#FFFFFF")


    canvas = Canvas(
        flu_dewasa,
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
        581.0,
        33.0,
        anchor="nw",
        text="FLU",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        flu_dewasa,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=fluToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_45.png"))
    button_45 = Button(
        flu_dewasa,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_45.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_46.png"))
    button_46 = Button(
        flu_dewasa,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_46.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    flu_dewasa.resizable(False, False)
    flu_dewasa.mainloop()
    
def radangAnak():
    global radang_anak
    def jumlahPesanan1():
        global jumlah
        
        radang_anak.destroy()
        nama_obat = "Troches (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Radang"]["Troches (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToRadang,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        radang_anak.destroy()
        nama_obat = "Proris (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Radang"]["Proris (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToRadang,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()

    
    radang_anak = Toplevel()
    radang_anak.geometry("1280x720")
    radang_anak.configure(bg = "#FFFFFF")


    canvas = Canvas(
        radang_anak,
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
        532.0,
        33.0,
        anchor="nw",
        text="RADANG",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        radang_anak,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=radangToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_43.png"))
    button_43 = Button(
        radang_anak,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_43.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_44.png"))
    button_44 = Button(
        radang_anak,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_44.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    radang_anak.resizable(False, False)
    radang_anak.mainloop()

def radangDewasa():
    global radang_dewasa
    def jumlahPesanan1():
        global jumlah
        
        radang_dewasa.destroy()
        nama_obat = "Strepsils"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Radang"]["strepsils"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToRadang,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        radang_dewasa.destroy()
        nama_obat = "Troches"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Radang"]["Troches"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToRadang,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
 
    
    radang_dewasa = Toplevel()
    radang_dewasa.geometry("1280x720")
    radang_dewasa.configure(bg = "#FFFFFF")


    canvas = Canvas(
        radang_dewasa,
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
        532.0,
        33.0,
        anchor="nw",
        text="RADANG",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        radang_dewasa,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=radangToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_47.png"))
    button_47 = Button(
        radang_dewasa,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_47.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_48.png"))
    button_48 = Button(
        radang_dewasa,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_48.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    radang_dewasa.resizable(False, False)
    radang_dewasa.mainloop()

def pilekAnak():
    global pilek_anak
    def jumlahPesanan1():
        global jumlah

        pilek_anak.destroy()
        nama_obat = "Ibuprofen (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Pilek"]["Ibuprofen (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPilek,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        global jumlah
        
        pilek_anak.destroy()
        nama_obat = "Sterimar (Anak)"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_anak"]["Pilek"]["Sterimar (Anak)"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPilek,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()

    
    pilek_anak = Toplevel()
    pilek_anak.geometry("1280x720")
    pilek_anak.configure(bg = "#FFFFFF")


    canvas = Canvas(
        pilek_anak,
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
        563.0,
        33.0,
        anchor="nw",
        text="PILEK",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        pilek_anak,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=pilekToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_37.png"))
    button_37 = Button(
        pilek_anak,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_37.place(
        x=170.0,
        y=391.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_38.png"))
    button_38 = Button(
        pilek_anak,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_38.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    pilek_anak.resizable(False, False)
    pilek_anak.mainloop()
    
def pilekDewasa():
    global pilek_dewasa
    def jumlahPesanan1():
        pilek_dewasa.destroy()
        nama_obat = "Mixagrip"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Pilek"]["Mixagrip"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPilek,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
   
    def jumlahPesanan2():
        pilek_dewasa.destroy()
        nama_obat = "Neozep forte"
        namaObat.append(nama_obat)
        harga_obat = obat["obat_dewasa"]["Pilek"]["Neozep forte"]
        hargaObat.append(harga_obat)
        def satu():
            jumlahPesan = 1
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def dua():
            jumlahPesan = 2
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def tiga():
            jumlahPesan = 3
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def empat():
            jumlahPesan = 4
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        def lima():
            jumlahPesan = 5
            jumlahPesanObat.append(jumlahPesan)
            total = harga_obat * jumlahPesan
            totalHarga.append(total)
            messagebox.showinfo("Berhasil!", "Obat berhasil ditambahkan!")
            jumlah.destroy()
            main.deiconify()
        
        jumlah = Toplevel()
        jumlah.geometry("1280x720")
        jumlah.configure(bg = "#FFFFFF")


        canvas = Canvas(
            jumlah,
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
        button_back_1 = PhotoImage(
            file=relative_to_assets("button_back.png"))
        button_back = Button(
            jumlah,
            image=button_back_1,
            borderwidth=0,
            highlightthickness=0,
            command=jumlahToPilek,
            relief="flat"
        )
        button_back.place(
            x=35.0,
            y=594.0,
            width=149.0,
            height=44.0
        )
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_angka1.png"))
        button_angka1 = Button(
            jumlah,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=satu,
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
            jumlah,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=dua,
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
            jumlah,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=tiga,
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
            jumlah,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=empat,
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
            jumlah,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lima,
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
        jumlah.resizable(False, False)
        jumlah.mainloop()
 
    
    pilek_dewasa = Toplevel()
    pilek_dewasa.geometry("1280x720")
    pilek_dewasa.configure(bg = "#FFFFFF")


    canvas = Canvas(
        pilek_dewasa,
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
        563.0,
        33.0,
        anchor="nw",
        text="PILEK",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        pilek_dewasa,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=pilekToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_25.png"))
    button_25 = Button(
        pilek_dewasa,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan2,
        relief="flat"
    )
    button_25.place(
        x=170.0,
        y=374.0,
        width=939.0,
        height=209.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_26.png"))
    button_26 = Button(
        pilek_dewasa,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=jumlahPesanan1,
        relief="flat"
    )
    button_26.place(
        x=170.0,
        y=139.0,
        width=939.0,
        height=209.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    pilek_dewasa.resizable(False, False)
    pilek_dewasa.mainloop()

def mainToAmbil():
    if len(namaObat) == 0:
        messagebox.showerror("Error!", "Pilih obat terlebih dahulu")
    else:
        main.withdraw()
        metodeAmbil()

def pengantaranToMain():
    pengantaran.destroy()
    main.deiconify()

def metodeAmbil():
    global pengantaran
    pengantaran = Toplevel()
    pengantaran.geometry("1280x720")
    pengantaran.configure(bg = "#FFFFFF")


    canvas = Canvas(
        pengantaran,
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
        950.9999728881904,
        576.2764278472241,
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
        443.0,
        71.0,
        anchor="nw",
        text="PESANAN ANDA",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        pengantaran,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=pengantaranToMain,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_49.png"))
    button_49 = Button(
        pengantaran,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=pilihDelivery,
        relief="flat"
    )
    button_49.place(
        x=298.0,
        y=390.0,
        width=618.0,
        height=67.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_50.png"))
    button_50 = Button(
        pengantaran,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=pilihPickUp,
        relief="flat"
    )
    button_50.place(
        x=298.0,
        y=218.0,
        width=610.0,
        height=72.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )
    pengantaran.resizable(False, False)
    pengantaran.mainloop()

def pilihPickUp():
    global metode
    metode = "Pick Up"
    pengantaran.destroy()
    pickup()

def pilihDelivery():
    global metode
    metode = "Delivery"
    pengantaran.destroy()
    delivery()

def pickupToPilih():
    pick_up.destroy()
    metodeAmbil()

def deliverToPilih():
    delivery_.destroy()
    metodeAmbil()

def pickup():
    global pick_up
    pick_up = Toplevel()
    pick_up.geometry("1280x720")
    pick_up.configure(bg = "#FFFFFF")

    def checkInputUser():
        global nama_pembeli
        global no_telepon
        nama_pembeli = str(entry_namapickup.get())
        no_telepon = int(entry_nopickup.get())
        if nama_pembeli == "" and no_telepon == "":
            messagebox.showerror("Error!", "Harap isi terlebih dahulu!")
        elif len(nama_pembeli) < 3:
            messagebox.showerror("Error!", "Nama minimal 4 huruf")
        elif no_telepon != int and len(str(no_telepon)) < 11:
            messagebox.showerror("Error!", "No telepon haruslah angka dan 12 digit!")
        else:
            pick_up.destroy()
            cetakStruk()
            showStruk()
            
    def tutup():
        struk.destroy()
        main.destroy()
        menu_utama()

    def showStruk():
        global struk
        struk = Toplevel()
        struk.geometry("300x600")
        struk.configure(bg = "#FFFFFF")
        struk.resizable(False, False)
        
        canvas= Canvas(struk, width= 300, height= 550, bg="#FFFFFF")
        canvas.create_text(150, 20, text=("="*10,"Struk Belanja","="*10), fill="black", font=('Helvetica 9'))
        y = 35
        for i in range(len(jumlahPesanObat)):
            canvas.create_text(37, y, text=f"\n{namaObat[i]}\nTotal Rp{hargaObat[i]*jumlahPesanObat[i]}", fill="black", font=('Helvetica 9'),anchor="w")
            canvas.create_text(263, y, text=f"Rp{hargaObat[i]} x {jumlahPesanObat[i]}", fill="black", font=('Helvetica 9'),anchor="e")
            y += 30
        canvas.create_text(150, 485, text=("="*33), fill="black", font=('Helvetica 9'))
        canvas.create_text(37, 500, text=f"{metode}", fill="black", font=('Helvetica 9'), anchor="w")
        canvas.create_text(37, 520, text=f"Total Semua: Rp{sum(totalHarga)}", fill="black", font=('Helvetica 9'), anchor='w')
        
        canvas.pack()
        button = Button(struk, 
                    text="Tutup", 
                    command= tutup)

        button.pack(padx=10, pady=10)
        
        struk.mainloop()
    
    def cetakStruk():
        day = str(datetime.now().strftime('%A'))
        time = str(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        with open("strukbelanja.csv", "a") as file:
            file.write(f"-"*37)
            file.write(f"\nAtas nama: {nama_pembeli}\n")
            file.write(f"No Telp.: {no_telepon}\n")
            file.write(f"{day}, {time}\n")
            file.write("============ Struk Belanja ===========\n")
            for i in range(0, len(jumlahPesanObat)):
                hargaDanJumlah = f"Rp {hargaObat[i]} x {jumlahPesanObat[i]}"
                obatName = f"{namaObat[i]}"
                file.write(f"{obatName.ljust(15)} {hargaDanJumlah.rjust(20)}\n")
                file.write(f"Total: {totalHarga[i]}\n")
            file.write("======================================\n")
            file.write(f"{metode}\n")
            file.write(f"Total {sum(totalHarga)}\n")
        
                
    canvas = Canvas(
        pick_up,
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
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        pick_up,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=pickupToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        pick_up,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=checkInputUser,
        relief="flat"
    )
    button_1.place(
        x=517.0,
        y=604.0,
        width=173.0,
        height=53.0
    )

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
        pick_up,
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
        pick_up,
        bd=0,
        bg="#09979D",
        fg="#000716",
        highlightthickness=0
    )
    entry_nopickup.place(
        x=317.0,
        y=387.0,
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
    
    pick_up.resizable(False, False)
    pick_up.mainloop()
    
def delivery():
    global delivery_
    delivery_ = Toplevel()
    delivery_.geometry("1280x720")
    delivery_.configure(bg = "#FFFFFF")
    
    def checkInputUser():
        global nama_pembeli
        global no_telepon
        global alamat
        nama_pembeli = str(entry_1.get())
        no_telepon = int(entry_3.get())
        alamat = str(entry_2.get())
        if nama_pembeli == "" and no_telepon == "" and alamat == "":
            messagebox.showerror("Error!", "Harap isi terlebih dahulu!")
        elif len(nama_pembeli) < 3:
            messagebox.showerror("Error!", "Nama minimal 4 huruf")
        elif no_telepon != int and len(str(no_telepon)) < 11:
            messagebox.showerror("Error!", "No telepon haruslah angka dan 12 digit!")
        elif 'Jalan' in alamat == False or 'Jl.' in alamat == False:
            messagebox.showerror("Error!", "Masukkan Alamat yang benar!")
        else:
            cetakStruk()
            delivery_.destroy()
            showStruk()
    
    def tutup():
        struk.destroy()
        main.destroy()
        menu_utama()

    def showStruk():
        global struk
        struk = Toplevel()
        struk.geometry("300x600")
        struk.configure(bg = "#FFFFFF")
        struk.resizable(False, False)
        
        canvas= Canvas(struk, width= 300, height= 550, bg="#FFFFFF")
        canvas.create_text(150, 20, text=("="*10,"Struk Belanja","="*10), fill="black", font=('Helvetica 9'))
        y = 35
        for i in range(len(jumlahPesanObat)):
            canvas.create_text(37, y, text=f"\n{namaObat[i]}\nTotal Rp{hargaObat[i]*jumlahPesanObat[i]}", fill="black", font=('Helvetica 9'),anchor="w")
            canvas.create_text(263, y, text=f"Rp{hargaObat[i]} x {jumlahPesanObat[i]}", fill="black", font=('Helvetica 9'),anchor="e")
            y += 30
        canvas.create_text(150, 485, text=("="*33), fill="black", font=('Helvetica 9'))
        canvas.create_text(37, 500, text=f"{metode}", fill="black", font=('Helvetica 9'), anchor="w")
        canvas.create_text(37, 520, text=f"Total Semua: Rp{sum(totalHarga)}", fill="black", font=('Helvetica 9'), anchor='w')
        
        canvas.pack()
        button = Button(struk, 
                    text="Tutup", 
                    command= tutup)

        button.pack(padx=10, pady=10)
        
        struk.mainloop()
    
    def cetakStruk():
        day = str(datetime.now().strftime('%A'))
        time = str(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        with open("strukbelanja.csv", "a") as file:
            file.write(f"-"*37)
            file.write(f"\nAtas nama: {nama_pembeli}\n")
            file.write(f"No Telp.: {no_telepon}\n")
            file.write("============== Struk Belanja =============\n")
            file.write(f"{day}, {time}\n")
            for i in range(0, len(jumlahPesanObat)):
                hargaDanJumlah = f"Rp {hargaObat[i]} x {jumlahPesanObat[i]}"
                file.write(f"{namaObat[i]} {hargaDanJumlah.rjust(23)}\n")
                file.write(f"Total: {totalHarga[i]}\n")
            file.write("==========================================\n")
            file.write(f"{metode} to {alamat}\n")
            file.write(f"Total {sum(totalHarga)}\n")
    
    
    canvas = Canvas(
        delivery_,
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
        517.0,
        71.0,
        anchor="nw",
        text="DELIVERY",
        fill="#FFFFFF",
        font=("Inter Bold", 35 * -1)
    )
    button_back_1 = PhotoImage(
    file=relative_to_assets("button_back.png"))
    button_back = Button(
        delivery_,
        image=button_back_1,
        borderwidth=0,
        highlightthickness=0,
        command=deliverToPilih,
        relief="flat"
    )
    button_back.place(
        x=35.0,
        y=594.0,
        width=149.0,
        height=44.0
    )
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        92.0,
        74.0,
        image=image_image_2
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        604.5,
        233.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        delivery_,
        bd=0,
        bg="#09979D",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=318.0,
        y=189.0,
        width=573.0,
        height=78.0
    )

    canvas.create_text(
        303.0,
        157.0,
        anchor="nw",
        text="Nama: ",
        fill="#09679D",
        font=("Kadwa Regular", 20 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        604.5,
        363.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        delivery_,
        bd=0,
        bg="#09979D",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=318.0,
        y=319.0,
        width=573.0,
        height=78.0
    )

    canvas.create_text(
        303.0,
        287.0,
        anchor="nw",
        text="Alamat: ",
        fill="#09679D",
        font=("Kadwa Regular", 20 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        604.5,
        503.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        delivery_,
        bd=0,
        bg="#09979D",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=318.0,
        y=459.0,
        width=573.0,
        height=78.0
    )

    canvas.create_text(
        303.0,
        427.0,
        anchor="nw",
        text="No. Telepon: ",
        fill="#09679D",
        font=("Kadwa Regular", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        delivery_,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=checkInputUser,
        relief="flat"
    )
    button_1.place(
        x=518.0,
        y=603.0,
        width=173.0,
        height=53.0
    )
    
    delivery_.resizable(False, False)
    delivery_.mainloop()

if __name__ == "__main__":
    loginAccount() 