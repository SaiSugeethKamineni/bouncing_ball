 # -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:06:19 2016

@author: sai_sugeeth_kamineni
"""

import tkinter as tk
#import sys
root = tk.Tk()

root.title("Gravity bouncing ball")

cw = 500
ch = 400


canvas = tk.Canvas(root, width = cw, height = ch, bg = 'cyan')
canvas.grid()
Dt = 0.041
g = 1000
e = 0.3

rl = 300
rb = 100

stop = 0
x = 0

class ball():
    def __init__(self, x, y, vx, vy, colour):
        self.diameter = 20
        self.x = x
        self.y = y
        self.colour = colour
        
        if self.x >= cw - self.diameter/2.0:
            self.x = cw - self.diameter/2.0
            self.vx = -(abs(vx)*(1-e))
            print ("\a")
        elif self.x <= self.diameter/2.0:
            self.x = self.diameter/2.0
            self.vx = -(abs(vx)*(1-e))
            print ("\a")
        elif self.x <= rb + self.diameter/2.0 and self.y > 100:
            self.x = rb + self.diameter/2.0
            self.vx = -vx*(1-e)
            print ("\a")
        else:
            self.vx = vx
        
        if self.y >= ch - self.diameter/2.0:
            self.y = ch - self.diameter/2.0
            self.vy = -abs(vy)*(1-e)
            print("\a")
        elif self.y <= self.diameter/2.0:
            self.y = self.diameter/2.0
            self.vy = -vy
            print ("\a")
        else:
            self.vy = vy + g*Dt
            
Ball = ball(100, 89, 250, 0, "blue")

def start_frame():
    global Ball, stop    
    Ball = ball(100, 89, 250, 0, "blue")
    stop = 0
    while stop != 1:
        canvas.create_rectangle(0, 100, 100, 400, fill = 'red')
        canvas.create_oval(Ball.x - Ball.diameter/2.0, Ball.y - Ball.diameter/2.0,  Ball.x + Ball.diameter/2.0, Ball.y + Ball.diameter/2.0, fill = Ball.colour)
        Ball = ball(Ball.x+Ball.vx*Dt, Ball.y+Ball.vy*Dt, Ball.vx, Ball.vy, Ball.colour)
        canvas.update()
        canvas.after(41)
        canvas.delete(tk.ALL)

def ball_frame():
    global Ball, stop
    stop = 0
    while stop != 1:
        canvas.create_rectangle(0, 100, 100, 400, fill = 'red')
        canvas.create_oval(Ball.x - Ball.diameter/2.0, Ball.y - Ball.diameter/2.0,  Ball.x + Ball.diameter/2.0, Ball.y + Ball.diameter/2.0, fill = Ball.colour)
        Ball = ball(Ball.x+Ball.vx*Dt, Ball.y+Ball.vy*Dt, Ball.vx, Ball.vy, Ball.colour)
        canvas.update()
        canvas.after(41)
        canvas.delete(tk.ALL)
        
        
def end_frame():
    global Ball, stop
    stop = 1
    while stop == 1:
        canvas.create_rectangle(0, 100, 100, 400, fill = 'red')
        canvas.create_oval(Ball.x - Ball.diameter/2.0, Ball.y - Ball.diameter/2.0,  Ball.x + Ball.diameter/2.0, Ball.y + Ball.diameter/2.0, fill = Ball.colour)
        canvas.update()
        canvas.after(41)
        canvas.delete(tk.ALL)

def quit_frame():
    root.destroy()

button_1 = tk.Button(text = "Start", padx = 10, pady = 10)
button_1.config(cursor = 'gumby', bd = 8, relief = "raised", bg = "blue", fg = 'black', font = ('helvetica', 20, 'underline italic'), command = start_frame)
button_1.grid(row = 1, column = 1)

button_2 = tk.Button(text = "Freeze", padx =10, pady = 10 )
button_2.config(cursor = 'gumby', bd = 8, relief = "raised", bg = "blue", fg = 'black', font = ('helvetica', 20, 'underline italic'), command = end_frame)
button_2.grid(row = 2, column = 1)

button_3 = tk.Button(text = "Quit", padx = 10, pady = 10)
button_3.config(cursor = 'gumby', bd = 8, relief = "raised", bg = "blue", fg = 'black', font = ('helvetica', 20, 'underline italic'), command = quit_frame)
button_3.grid(row = 4, column = 1)

button_4 = tk.Button(text = "Unfreeze", padx = 10, pady = 10)
button_4.config(cursor = 'gumby', bd = 8, relief = "raised", bg = "blue", fg = 'black', font = ('helvetica', 20, 'underline italic'), command = ball_frame)
button_4.grid(row = 3, column = 1)

while x == 0:
    canvas.create_rectangle(0, 100, 100, 400, fill = 'red')
    canvas.create_oval(Ball.x - Ball.diameter/2.0, Ball.y - Ball.diameter/2.0,  Ball.x + Ball.diameter/2.0, Ball.y + Ball.diameter/2.0, fill = Ball.colour)
    canvas.update()
    canvas.after(41)
    canvas.delete(tk.ALL)

root.mainloop()


        
        

