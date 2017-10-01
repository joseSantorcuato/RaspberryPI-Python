#Taller e&m
# -*- coding: utf-8 -*-
from Tkinter import *

mi_gui = Tk()
mi_gui.geometry("500x500") #Tamano ancho y alto
mi_gui.resizable() #Se puede redimensionar, mi_gui.resizable(0,0) no se dimensiona
var = StringVar()
label = Label( mi_gui, textvariable=var, relief= FLAT )# probar  RAISED en relief

var.set("Estamos trabajando con Tkinter")
label.pack()
mi_gui.mainloop()
