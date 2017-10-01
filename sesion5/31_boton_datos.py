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
#mi_tiempo = time.asctime( time.localtime(time.time()) )
#mi_tiempob = calendar.month(2017, 9)funcion de calendar
#mi_tiempoc = str(time.time())
#mi_tiempod = strftime("%Y-%m-%d %H:%M:%S", gmtime())
fecha = strftime("%Y-%m-%d", gmtime())
hora_actual = datetime.datetime.now()

ano = hora_actual.year
mes = hora_actual.month
dia = hora_actual.day
hora = hora_actual.hour
minu = hora_actual.minute
secu = hora_actual.second
# 2015 5 6 8 53 40
hora_completa = "La hora actual es "+str(hora)+":"+str(minu)

var = StringVar()
def accionBotonUno():
   tkMessageBox.showinfo( "Interaccion", ""+hora_completa)

micolor = '#%02x%02x%02x' % (100, 200, 100)
miboton = Button(mi_gui, text ="Presiona aca para comenzar", command = accionBotonUno)


marca = Label( mi_gui, textvariable=var,fg=micolor, font=(None, 12),height=2, width=30, relief= FLAT )# probar  RAISED en relief
var.set("Estamos trabajando con Tkinter\nEn el taller de Electronica y multimedia")
marca.config(anchor=W,justify=LEFT)
posx = 10
posy = 400
marca.place(x=posx,y=posy)
miboton.place(x=posx, y=200)


mi_gui.mainloop()
