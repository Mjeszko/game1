import tkinter
from tkinter import *
from tkinter import messagebox

def akcja():
   'tu ktoś ma wpisać skrypt aby guziki zmieniały swóje imię na X/O/puste'

def pomoc():
   Pomoc = Toplevel()
   Pomoc.title ('Pomoc')
   Pomoc.geometry ('500x300')
   labelpomoc = tkinter.Label(Pomoc, text='pomoc')
   labelpomoc.pack(side=tkinter.TOP) 
def oaplikacji():
   about = Toplevel()
   about.title ('O aplikacji')
   about.geometry ('500x300')
   labelabout = tkinter.Label(about, text='O GRZE :) niech tu ktoś wpisze jakieś info typu kto robił itd')
   labelabout.pack(side=tkinter.TOP)
def nowy():
   nic
def zakończ():
   zmienna = messagebox.askyesno('ZAMYKANIE','CZY CHCESZ ZAMKNAC PROGRAM?')
   if zmienna == True:
      Aplikacja.destroy()
      return
def cofnij():
   nic
Aplikacja = Tk()
Aplikacja.title ('Kółko i Krzyżyk')
Aplikacja.geometry ('280x300')
Aplikacja.resizable(0, 0)
pasekMenu = Menu(Aplikacja)



menuPlik = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Plik", menu=menuPlik)

menuPlik.add_command(label="Nowy", command=akcja)
menuPlik.add_separator()
menuPlik.add_command(label="Zakończ", command=zakończ)

menuEdycja = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Edycja", menu=menuEdycja)

menuEdycja.add_command(label="Conij", command=akcja)

menuHelp = Menu(pasekMenu, tearoff=0)
pasekMenu.add_cascade(label="Pomoc", menu=menuHelp)

menuHelp.add_command(label="Pomoc", command=pomoc)
menuHelp.add_separator()
menuHelp.add_command(label="O aplikacji...", command=oaplikacji)

Aplikacja.config(menu=pasekMenu)


przycisk = Button (height=5, width=10, text='',command=akcja).place (x=10,y=10)
przycisk2 = Button (height=5, width=10, text='',command=akcja).place (x=100,y=10)
przycisk3 = Button (height=5, width=10, text='',command=akcja).place (x=190,y=10)
przycisk4 = Button (height=5, width=10, text='',command=akcja).place (x=10,y=105)
przycisk5 = Button (height=5, width=10, text='',command=akcja).place (x=100,y=105)
przycisk6 = Button (height=5, width=10, text='',command=akcja).place (x=190,y=105)
przycisk7 = Button (height=5, width=10, text='',command=akcja).place (x=10,y=200)
przycisk8 = Button (height=5, width=10, text='',command=akcja).place (x=100,y=200)
przycisk9 = Button (height=5, width=10, text='',command=akcja).place (x=190,y=200)

Aplikacja.mainloop()
