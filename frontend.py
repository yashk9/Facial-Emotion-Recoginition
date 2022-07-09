import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os
from os.path import basename
import cv2

from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import numpy as np

my_w = tk.Tk()
my_w.geometry('1920x1080')
my_w.config(bg='#0B5A81')
my_w.title('Emotion Detection')
my_font1 = ('Times', 14)
# my_w['bg']='blue'

bg = PhotoImage(file=r"C:\Users\manvi moza\Desktop\ALL CODES\FERcodebase\changed.png")

my_label = Label(my_w, image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)

main_frame = Frame(my_w, bg='#21458a', relief=SOLID, padx=0, pady=0, borderwidth=1)

frame_bg = PhotoImage(file=r"C:\Users\manvi moza\Desktop\ALL CODES\FERcodebase\frame_back.png")

my_label1 = Label(main_frame, image=frame_bg)
my_label1.place(x=0,y=0,relheight=1,relwidth=1)

l1 = tk.Label(main_frame, text='EMOTION DETECTION SYSTEM', width=30, font="Helvetica 21 bold", background="#21458a", fg="#ffffff")

b1 = tk.Button(main_frame, text='Open Camera', width=20, command=lambda: camera_page(), font="Sans-serif 16",
               background="#21458a", fg="#ffffff", relief=RAISED)

l2 = tk.Message(main_frame, text='WARNING!! \n Please keep note that we would be storing your data. Thank you for cooperating!', width=580,
                justify="center" ,font="Arial 12 italic", background="#21458a", fg="#ffffff")

l1.grid(row=1, column=1, pady=10, padx=0)
b1.grid(row=2, column=1, pady=130, padx=0)

l2.grid(row=3, column=1, pady=0, padx=0)

#changes the entire postion of the frame.
main_frame.place(x=30, y=230)

def camera_page():
    # my_w.destroy()
    import camera

my_w.mainloop()
