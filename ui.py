#!/usr/bin/env python
#Python 2.7
#Tkinter

from main import *
#from Tkinter import *
from math import *

root = Tk()
root.title("Coin Flip")
root.configure(bg='grey')
width = 300
height = 450
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

Label (text = "Coin Flipping Simulator", bg = "#a21c1c", fg = 'White', width = "300", height = "2", justify = 'center', font = ("Calibri", '14', 'bold')).pack()

Label (root, text='', bg='grey').pack()  # blank space

Label (root, text='Enter the amount of flips', font = ('Calibri', '13', 'bold'), bg='grey').pack()

Label (root, text='', bg='grey').pack()  # blank space

e1 = Entry (root, text='number', width='10', relief=FLAT)
e1.pack() 

global heads
global tails
global head_percentage
global tails_percentage

def calculate():

    heads = str(main(int(e1.get()))[0].get('Heads'))
    tails = str(main(int(e1.get()))[0].get('Tails'))
    heads_percentage = str(main(int(e1.get()))[3])
    tails_percentage = str(main(int(e1.get()))[4])

    Label(root, text='\nHeads: ' + heads, bg='grey').pack()

    Label(root, text='Tails: ' + tails, bg='grey').pack()

    Label(root, text='-'*15, bg='grey').pack()

    Label(root, text='Heads percentage: ' + heads_percentage + '%', bg='grey').pack()

    Label(root, text='Tails percentage: ' + tails_percentage + '%', bg='grey').pack()

Label (root, text='', bg='grey').pack()  # blank space

Button (root, text='Calculate', activebackground = '#a21c1c', activeforeground = 'white', relief = FLAT, command=calculate).pack()

Label (root, text='', bg='grey').pack()  # blank space

Label (root, text='Results', bg='grey').pack()

Label (root, text='Version  -  @ 1.2.0', font = ('Calibri', '10', 'bold'), bg = '#a21c1c', fg = 'White', width = '300', height = '1',).pack(side = BOTTOM)

root.mainloop()
