#Taller e&m
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox


root = Tk()
root.geometry("500x500") #Tamano ancho y alto
root.resizable() #Se puede redimensionar, root.resizable(0,0) no se dimensiona

var = StringVar()
def accionBotonUno():
   tkMessageBox.showinfo( "Interaccion", "El boton funciona")

micolor = '#%02x%02x%02x' % (100, 200, 100)
miboton = Button(root, text ="Presiona aca para comenzar", command = accionBotonUno)


marca = Label( root, textvariable=var,fg=micolor, font=(None, 12),height=2, width=30, relief= FLAT )# probar  RAISED en relief
var.set("Estamos trabajando con Tkinter\nEn el taller de Electronica y multimedia")
marca.config(anchor=W,justify=LEFT)
posx = 10
posy = 400
marca.place(x=posx,y=posy)
miboton.place(x=posx, y=200)


root.mainloop()
