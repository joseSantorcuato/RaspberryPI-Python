#Taller e&m
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from time import *
import datetime
import calendar

mi_gui = Tk()
mi_gui.geometry("500x500") #Tamano ancho y alto
mi_gui.resizable() #Se puede redimensionar, mi_gui.resizable(0,0) no se dimensiona

var = StringVar()
def accionBotonUno():
   hora_actual = datetime.datetime.now()
   hora = hora_actual.hour
   minu = hora_actual.minute
   secu = hora_actual.second
   hora_completa = "La hora actual es "+str(hora)+":"+str(minu)+":"+str(secu)
   tkMessageBox.showinfo( "Interaccion",mientrada.get()+ "\n"+hora_completa)
   sleep(0.1)

micolor = '#%02x%02x%02x' % (100, 100, 100)
mientrada = Entry(mi_gui, bd =0.5)
miboton = Button(mi_gui, text ="Continuar", command = accionBotonUno)

marca = Label( mi_gui, textvariable=var,fg=micolor, font=(None, 12),height=2, width=40, relief= FLAT )# probar  RAISED en relief
var.set("Probando interacciones,\nIngresa tu nombre y presione continuar")
marca.config(anchor=W,justify=LEFT)

posx = 10
posy = 400
marca.place(x=posx,y=posy/4)
miboton.place(x=posx, y=200)
mientrada.place(x=posx, y=150)
mi_gui.mainloop()
