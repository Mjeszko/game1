import tkinter
from tkinter import *
from tkinter import messagebox

def pomoc():
   Pomoc = Toplevel()
   Pomoc.title ('Pomoc')
   Pomoc.geometry ('500x300')
   labelpomoc = tkinter.Label(Pomoc, text='\n\n\n\n\n\n\n\n Kliknij na przycisk, aby zmienił się w X, O lub puste pole.\n W razie czego, skorzystaj z opcji "Cofnij" albo "Nowy"')
   labelpomoc.pack(side=tkinter.TOP) 
def oaplikacji():
   about = Toplevel()
   about.title ('O aplikacji')
   about.geometry ('500x300')
   labelabout = tkinter.Label(about, text='\n\n\n\n\n\n Aplikacja stworzona przez grupe studentow\n Uniwersytetu Kazimierza Wielkiego w Bydgoszczy\n w ramach zaliczenia zajęć z\n Wprowadzenia do programowania obiektowego (Python/Java)\n w składzie: Milosz Krupa, Zaneta Lowicka, Maja Prezner, Zuzanna Sugier.')
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

def bttn1x():
   przyciskx = Button (height=5, width=10, text='X',command=bttn1o).place (x=10,y=10)
def bttn1o():
   przycisko = Button (height=5, width=10, text='O',command=bttn).place (x=10,y=10)
def bttn():
   przycisk = Button (height=5, width=10, text='',command=bttn1x).place (x=10,y=10)

def bttn2x():
   przycisk2x = Button (height=5, width=10, text='X',command=bttn2o).place (x=100,y=10)
def bttn2o():
   przycisk2o = Button (height=5, width=10, text='O',command=bttn2).place (x=100,y=10)
def bttn2():
   przycisk2 = Button (height=5, width=10, text='',command=bttn2x).place (x=100,y=10)

def bttn3x():
   przycisk3x = Button (height=5, width=10, text='X',command=bttn3o).place (x=190,y=10)
def bttn3o():
   przycisk3o = Button (height=5, width=10, text='O',command=bttn3).place (x=190,y=10)
def bttn3():
   przycisk3 = Button (height=5, width=10, text='',command=bttn3x).place (x=190,y=10)
def bttn4x():
   przycisk4x = Button (height=5, width=10, text='X',command=bttn4o).place (x=10,y=105)
def bttn4o():
   przycisk4o = Button (height=5, width=10, text='O',command=bttn4).place (x=10,y=105)
def bttn4():
   przycisk4 = Button (height=5, width=10, text='',command=bttn4x).place (x=10,y=105)

def bttn5x():
   przycisk5x = Button (height=5, width=10, text='X',command=bttn5o).place (x=100,y=105)
def bttn5o():
   przycisk5o = Button (height=5, width=10, text='O',command=bttn5).place (x=100,y=105)
def bttn5():
   przycisk5 = Button (height=5, width=10, text='',command=bttn5x).place (x=100,y=105)

def bttn6x():
   przycisk6x = Button (height=5, width=10, text='X',command=bttn6o).place (x=190,y=105)
def bttn6o():
   przycisk6o = Button (height=5, width=10, text='O',command=bttn6).place (x=190,y=105)
def bttn6():
   przycisk6 = Button (height=5, width=10, text='',command=bttn6x).place (x=190,y=105)
def bttn7x():
   przycisk7x = Button (height=5, width=10, text='X',command=bttn7o).place (x=10,y=200)
def bttn7o():
   przycisk7o = Button (height=5, width=10, text='O',command=bttn7).place (x=10,y=200)
def bttn7():
   przycisk7 = Button (height=5, width=10, text='',command=bttn7x).place (x=10,y=200)

def bttn8x():
   przycisk8x = Button (height=5, width=10, text='X',command=bttn8o).place (x=100,y=200)
def bttn8o():
   przycisk8o = Button (height=5, width=10, text='O',command=bttn8).place (x=100,y=200)
def bttn8():
   przycisk8 = Button (height=5, width=10, text='',command=bttn8x).place (x=100,y=200)

def bttn9x():
   przycisk9x = Button (height=5, width=10, text='X',command=bttn9o).place (x=190,y=200)
def bttn9o():
   przycisk9o = Button (height=5, width=10, text='O',command=bttn9).place (x=190,y=200)
def bttn9():
   przycisk9 = Button (height=5, width=10, text='',command=bttn9x).place (x=190,y=200)


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


przycisk = Button (height=5, width=10, text='',command=bttn1x).place (x=10,y=10)
przycisk2 = Button (height=5, width=10, text='',command=bttn2x).place (x=100,y=10)
przycisk3 = Button (height=5, width=10, text='',command=bttn3x).place (x=190,y=10)
przycisk4 = Button (height=5, width=10, text='',command=bttn4x).place (x=10,y=105)
przycisk5 = Button (height=5, width=10, text='',command=bttn5x).place (x=100,y=105)
przycisk6 = Button (height=5, width=10, text='',command=bttn6x).place (x=190,y=105)
przycisk7 = Button (height=5, width=10, text='',command=bttn7x).place (x=10,y=200)
przycisk8 = Button (height=5, width=10, text='',command=bttn8x).place (x=100,y=200)
przycisk9 = Button (height=5, width=10, text='',command=bttn9x).place (x=190,y=200)

Aplikacja.mainloop()
