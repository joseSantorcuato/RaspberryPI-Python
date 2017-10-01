#Taller e&m
# -*- coding: utf-8 -*-
from Tkinter import *

mi_gui = Tk()
mi_gui.geometry("500x500") #Tamano ancho y alto
mi_gui.resizable() #Se puede redimensionar, mi_gui.resizable(0,0) no se dimensiona

var = StringVar()

micolor = '#%02x%02x%02x' % (122, 12, 208)

marca = Label( mi_gui, textvariable=var,fg=micolor, font=(None, 12),height=2, width=30, relief= FLAT )# probar  RAISED en relief
var.set("Estamos trabajando con Tkinter\nEn el taller de Electronica y multimedia")
marca.config(anchor=W,justify=LEFT)
posx = 10
posy = 400
marca.place(x=posx,y=posy)


mi_gui.mainloop()
