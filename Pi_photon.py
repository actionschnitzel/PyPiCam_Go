from tkinter import *
from os import popen
from os import system as cmd
from PIL import ImageTk, Image
from pathlib import Path
from tkinter import ttk

# import picamera
# from picamera import *
from time import sleep


home = str(Path.home())
print(f"{home} is your home directory!")


class PyPiCam_Go:
    def __init__(self, main):
        self.main = main
        main.title("PyPiCam_Go")

        # Header_Image
        self.welcome_icon = PhotoImage(file=r"~/PyPiCam_GO/Pi-Camera.png")
        self.head_frame = Frame().pack()
        self.header_label = Label(self.head_frame, image=self.welcome_icon).pack()

        # Clicker_Frame
        self.btn_frame = Frame().pack()
        self.label = Label(
            self.btn_frame,
            text="Files will be saved in /home/pi/PyPiCam_Go\nGive it a Name",
        )
        self.label.pack()

        self.entry = Entry(self.btn_frame, bd=5, width=31, borderwidth=1)
        self.entry.pack()
        self.photo_btn = Button(
            self.btn_frame, text="Take A Photo", command=self.photo1
        )
        self.photo_btn.pack()

        self.video_btn = Button(
            self.btn_frame, text="Take A Photo", command=self.video1
        )
        self.video_btn.pack()

        self.close_button = Button(self.btn_frame, text="Close", command=main.destroy)
        self.close_button.pack()

    def photo1(self):
        photo = str(self.entry.get())
        popen(f"libcamera-jpeg -o {home}/PyPiCam_GO/{photo}.jpg")

    def video1(self):
        video = str(self.entry.get())
        popen(f"libcamera-vid -t 10000 -o {home}/PyPiCam_GO/{video}.h264")


root = Tk()
my_gui = PyPiCam_Go(root)
root.mainloop()
