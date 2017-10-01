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
   fecha = strftime("%Y-%m-%d", gmtime())
   hora_actual = datetime.datetime.now()

   hora = hora_actual.hour
   minu = hora_actual.minute
   secu = hora_actual.second
   # 2015 5 6 8 53 40
   hora_completa = "La hora actual es "+str(hora)+":"+str(minu)+":"+str(secu)
   tkMessageBox.showinfo( "Interaccion", ""+hora_completa)
   sleep(0.1)
   """
   f = open('log.txt','w')
   f.write('Hora:'+str(hora_completa)+"\n")
   f.close()
   """

with open('log.txt', 'a') as file:
    fecha = strftime("%Y-%m-%d", gmtime())
    hora_actual = datetime.datetime.now()

    hora = hora_actual.hour
    minu = hora_actual.minute
    secu = hora_actual.second
    # 2015 5 6 8 53 40
    hora_completa = "La hora actual es "+str(hora)+":"+str(minu)+":"+str(secu)+"\n"
    file.write(hora_completa)
    file.close()
micolor = '#%02x%02x%02x' % (100, 200, 100)
miboton = Button(mi_gui, text ="Presiona aca para comenzar", command = accionBotonUno)

marca = Label( mi_gui, textvariable=var,fg=micolor, font=(None, 12),height=2, width=30, relief= FLAT )# probar  RAISED en relief
var.set("Probando interacciones, generando txt")
marca.config(anchor=W,justify=LEFT)
posx = 10
posy = 400
marca.place(x=posx,y=posy)
miboton.place(x=posx, y=200)


mi_gui.mainloop()
