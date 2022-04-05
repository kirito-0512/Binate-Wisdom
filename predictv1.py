# -*- coding: utf-8 -*-
"""

@author: Hrudai Aditya
"""

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog
import os
from PIL import Image,ImageTk,ImageDraw,ImageFont
import cv2
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization,AveragePooling2D,Convolution2D
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.optimizers import Adam
from keras.utils.vis_utils import plot_model
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split

from keras.models import model_from_json

#load model
model = model_from_json(open("C:/Users/Hrudai Aditya/Desktop/sw/proj3/cnnv2/sih.json", "r").read())
#load weights
model.load_weights('C:/Users/Hrudai Aditya/Desktop/sw/proj3/cnnv2/sih.h5')
    
window = tk.Tk()
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.configure(bg = 'blanched almond')
window.title("APPLICATION FORM")
msg = tk.Label(text = "APPLICATION FORM",font = ("Algerian",30),bg = 'blanched almond')
msg.place(x=430,y=10)
w = Canvas(window, width=1325, height=30,bg='blanched almond',highlightthickness=0)
w.create_line(15, 25, 10000, 25,width=2)
w.place(x=0,y=50)

#global img_ph,img_si,temp
def open1():    
    global file_path1
    file_path1 = filedialog.askopenfilename()
    #print(file_path1)
    ph = open(file_path1, "rb")
    photo=Image.open(ph)
    rload=photo.resize((250,250))
    render = ImageTk.PhotoImage(rload)
    img_ph = Label(window, image=render)
    img_ph.image=render
    img_ph.place(x=100, y=400)
    image_label=Label(window,text="Photo uploaded successfully",font=('Times 18'),width=25, height=1)
    image_label.place(x = 50, y =700)

    
def open2():
    global file_path2
    file_path2 = filedialog.askopenfilename()
    #print(file_path2)
    si = open(file_path2, "rb")
    sign=Image.open(si)
    rload=sign.resize((250,250))
    render = ImageTk.PhotoImage(rload)
    img_si = Label(window, image=render)
    img_si.image=render
    img_si.place(x=1200, y=400)
    global signature_label
    signature_label=Label(window,text="Signature uploaded successfully",font=('Times 18'),width=25, height=1)
    signature_label.place(x = 1150, y =700)

def check():
    img=cv2.imread(file_path1)
    imgnew = cv2.resize(img, (200, 200),3)

    imgnew = img_to_array(imgnew)
    imgnew = np.expand_dims(imgnew, axis=0)
    
    preds=model.predict(imgnew)[0]
    output=np.argmax(preds)
    count=output
    img1=cv2.imread(file_path2)
    imgnew1= cv2.resize(img1, (200, 200),3)

    imgnew1 = img_to_array(imgnew1)
    imgnew1 = np.expand_dims(imgnew1, axis=0)
    
    preds1=model.predict(imgnew1)[0]
    output1=np.argmax(preds1)
    print(output1)
    count1=output1

    if(count==0 and count1==0):
        error_label=Label(window,text="INSERT ONLY ONE PHOTO",font=('Times 18'),width=30, height=1)
        error_label.place(x = 500, y =700)
    elif (count!=0 and count1!=0):
        error_label=Label(window,text="INSERT ONLY ONE SIGNATURE",font=('Times 18'),width=30, height=1)
        error_label.place(x = 500, y =700)
    elif (count!=0 and count1==0):
        error_label=Label(window,text="Submitted Successfully",font=('Times 18'),width=30, height=1)
        error_label.place(x = 500, y =700)
        swap()
    elif (count==0 and count1!=0):
        error_label=Label(window,text="Submitted Successfully",font=('Times 18'),width=30, height=1)
        error_label.place(x = 500, y =700)
        display()
    #else:
    #    display()
    cv2.imwrite("face_detected.png", img) 
    print(count)
    print('Successfully saved')
    
def swap(): 
    #function to swap locations of images
    global file_path1
    global file_path2
    file_path1,file_path2=file_path2,file_path1
    #print(file_path1,file_path2)
    display()
def display():
    new_window = Toplevel(window)
    width= new_window.winfo_screenwidth()               
    height= new_window.winfo_screenheight()               
    new_window.geometry("%dx%d" % (width, height))
    #new_window.geometry("1800x900")
    window.title("NEW WINDOW")
    msg = tk.Label(new_window,text = "\tADMIT CARD\t",font = ("Algerian",30),bg = 'gray76')
    msg.place(x=430,y=10)
    new_window.configure(bg = 'gray76')
    global fname_new
    global lname_new
    global mail_new
    global fname_label_new
    global lname_label_new
    global mail_label_new
    fname_label_new=Label(new_window,text="First Name",font=('Times 18'),width=10, height=1)
    fname_label_new.place(x = 100, y = 75)
    lname_label_new=Label(new_window,text="Last Name",font=('Times 18'),width=10, height=1)
    lname_label_new.place(x = 100, y = 150)
    mail_label_new=Label(new_window,text="Email",font=('Times 18'),width=10, height=1)
    mail_label_new.place(x = 80, y = 250)
    fname_new=Label(new_window,text=fname.get(),font=('Times 18'),width=10, height=1)
    fname_new.place(x = 400, y = 75)
    lname_new=Label(new_window,text=lname.get(),font=('Times 18'),width=10, height=1)
    lname_new.place(x = 400, y = 150)
    mail_new=Label(new_window,text=mail.get(),font=('Times 18'),width=25, height=1)
    mail_new.place(x = 350, y = 250)
    lname_new=Label(new_window,text="Candidate Photo",font=('Times 18'),width=25, height=1)
    lname_new.place(x = 50, y = 400)
    mail_new=Label(new_window,text="Candidate signature",font=('Times 18'),width=25, height=1)
    mail_new.place(x = 700, y = 400)
    photo=Image.open(file_path1)
    rload=photo.resize((250,250))
    render = ImageTk.PhotoImage(rload)
    img_ph = Label(new_window, image=render)
    img_ph.image=render
    img_ph.place(x=100, y=450)
    
    sign=Image.open(file_path2)
    rload2=sign.resize((250,250))
    render2 = ImageTk.PhotoImage(rload2)
    img_si = Label(new_window, image=render2)
    img_si.image=render2
    img_si.place(x=725, y=450)
    new_window.mainloop()
global fname
global lname
global mail
global fname_label
global lname_label
global mail_label
#create text boxes
fname=Entry(window,width=30,font=('Georgia 20'))
fname.place(x = 150, y = 100,width=300,height=40)
lname=Entry(window,width=30,font=('Georgia 20'))
lname.place(x = 610, y = 100,width=300,height=40)
mail=Entry(window,width=30,font=('Georgia 20'))
mail.place(x = 1060, y = 100,width=300,height=40)

#create TextBox Labels
fname_label=Label(window,text="First Name",font=('Times 18'),width=10, height=1)
fname_label.place(x = 0, y = 105)
lname_label=Label(window,text="Last Name",font=('Times 18'),width=10, height=1)
lname_label.place(x = 460, y = 105)
mail_label=Label(window,text="Email",font=('Times 18'),width=10, height=1)
mail_label.place(x = 915, y = 105)
ph_label=Label(window,text="Upload Photo",font=('Times 18'),width=15, height=1)
ph_label.place(x = 450, y = 265)
si_label=Label(window,text="Upload Signature",font=('Times 18'),width=15, height=1)
si_label.place(x = 450, y = 365)
b3 = tk.Button(window,height = 1,width = 8,text  = "Photo", font=("Times 18",20), command = open1,bg = "yellow" )
b4 = tk.Button(window,height = 1,width = 8,text  = "Sign", font=("Times 18",20),command = open2,bg = "yellow" )
b3.place(x = 750, y = 250)
b4.place(x = 750, y = 350)
b5 = tk.Button(window,height = 1,width = 8,text  = "Submit",font=("Times 18",20),command = check, bg = "red" )
b5.place(x = 600, y = 500)
window.mainloop()
