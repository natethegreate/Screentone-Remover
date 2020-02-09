# Feb 2020 - Nathan Cueto
# Attempt to remove screentones from input images (png) using blurring and sharpening
# 
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
import scipy.signal as signal
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from PIL import ImageFilter
import math
from matplotlib import pyplot as plt
from skimage.io import imread

# Gaussian blue with variable kernel size, aka more or less blurring
def blur(img, blur_amount=5):
    horiz_kernel = np.ones((blur_amount,blur_amount), np.float32)/ (blur_amount*blur_amount)
    dst = cv2.GaussianBlur(img,(blur_amount,blur_amount),0)
    dst = cv2.blur(dst,(3, 3))

    return dst

# Laplacian filter for sharpening. Only want to do runs of 3x3 kernels to avoid oversharpening.
def sharp(img, img2, sharp_amount = 5):
    s_kernel = np.array([[0,-1.14,0], [-1.14,5.7,-1.14], [0,-1.14,0]])

    sharpened = cv2.filter2D(img, -1, s_kernel)
    # Multiple runs if different blurring was used. Default, 1 extra run
    if sharp_amount>=5:
        sharpened = cv2.filter2D(sharpened, -1, s_kernel)
    if sharp_amount >5:
        sharpened = cv2.filter2D(sharpened, -1, s_kernel)
    
    # plt.subplot(121)
    # plt.imshow(img2)
    # plt.title('Original')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(122)
    # plt.imshow(sharpened)
    # plt.title('sharp')
    # plt.xticks([]), plt.yticks([])
    # plt.show()
    return sharpened

def removeScreentones(dir_i, dir_o, amount):
    print(dir_i)
    print(dir_o)
    print(amount)

dtext = ""
otext = ""

def dnewdir():
    dtext = filedialog.askdirectory(title='Choose directory for input .pngs')
    dvar.set(dtext)

def onewdir():
    otext = filedialog.askdirectory(title='Choose directory for output .pngs')
    ovar.set(otext)
if __name__ == "__main__":
    # img = cv2.imread('16.png')
    # bs_amount = 5

    # blur_img = blur(img, bs_amount)
    # sharp_img = sharp(blur_img, img, bs_amount)
    # success = cv2.imwrite('output2.png', sharp_img)

    # GUI codes
    root = Tk()
    root.title("Screentone Remover")


    tFrame = Frame(root)
    bFrame = Frame(root)

    dvar = StringVar(root)
    ovar = StringVar(root)
    0
    # directory label, entry, and button
    d_label = Label(tFrame, text = 'Input file directory: ')
    d_label.grid(row=1, sticky=E, padx=20, pady=20)
    d_entry = Entry(tFrame, textvariable = dvar)
    d_entry.grid(row=1, column=1)
    dir_button = Button(tFrame, text="Browse", command=dnewdir)
    dir_button.grid(row=1, column=2)
    
    # output directory label, entry, and button
    o_label = Label(tFrame, text = 'Output file directory: ')
    o_label.grid(row=2,sticky=E)
    o_entry = Entry(tFrame, textvariable=ovar)
    o_entry.grid(row=2, column=1)
    out_button = Button(tFrame, text="Browse", command=onewdir)
    out_button.grid(row=2, column=2)

    slideLabel = Label(bFrame, text = 'Removal amount: (Default is 2)')
    slideLabel.grid(row=0, padx=20)
    filtslide = Scale(bFrame, from_=1, to=3, orient=HORIZONTAL)
    filtslide.grid( columnspan=2)
    go_button = Button(bFrame, text="Go!", command = lambda: removeScreentones(d_entry.get(), o_entry.get(), filtslide.get()))
    go_button.grid( columnspan=2)
    root.geometry("400x300")
    tFrame.pack(fill="both", expand=True)
    bFrame.pack(fill="both", expand=True)

    # go_button.pack(side=RIGHT)
    root.mainloop()
    

    pass
