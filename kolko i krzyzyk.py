import tkinter
from tkinter import *
from tkinter import messagebox

przyciski = []
obecnyGracz = 'X'
ostatniRuch = -1

def przygotujOkno():
    global przyciski
    global obecnyGracz
    global ostatniRuch

    def pomoc():
        Pomoc = Toplevel()
        Pomoc.title ('Pomoc')
        Pomoc.geometry ('500x300')
        labelpomoc = tkinter.Label(Pomoc, text='\n\n\n\n\n\n\n\n Kliknij na przycisk, aby zmienił się w X lub O.\n W razie czego, skorzystaj z opcji "Cofnij" albo "Nowy"')
        labelpomoc.pack(side=tkinter.TOP)
    def oaplikacji():
        about = Toplevel()
        about.title ('O aplikacji')
        about.geometry ('500x300')
        labelabout = tkinter.Label(about, text='\n\n\n\n\n\n Aplikacja stworzona przez grupe studentow\n Uniwersytetu Kazimierza Wielkiego w Bydgoszczy\n w ramach zaliczenia zajęć z\n Wprowadzenia do programowania obiektowego (Python/Java)\n w składzie: Milosz Krupa, Zaneta Lowicka, Maja Prezner, Zuzanna Sugier.')
        labelabout.pack(side=tkinter.TOP)
    def nowy():
        restart = messagebox.askyesno('Nowa gra', 'Czy chcesz rozpoczac nowa gre?')
        if restart:
            czyscPlansze()
    def zakoncz():
        zmienna = messagebox.askyesno('ZAMYKANIE','CZY CHCESZ ZAMKNAC PROGRAM?')
        if zmienna == True:
            Aplikacja.destroy()
            return
    def cofnij():
        global ostatniRuch
        if ostatniRuch == -1:
            messagebox.showerror("Brak ruchu", "Nie można cofnąć.")
            return
        przyciski[ostatniRuch]['text'] = ''
        zmianaGracza()
        ostatniRuch = -1

    Aplikacja = Tk()
    Aplikacja.title ('Kółko i Krzyżyk')
    Aplikacja.geometry ('280x300')
    Aplikacja.resizable(0, 0)
    pasekMenu = Menu(Aplikacja)

    menuPlik = Menu(pasekMenu, tearoff=0)
    pasekMenu.add_cascade(label="Plik", menu=menuPlik)

    menuPlik.add_command(label="Nowy", command=nowy)
    menuPlik.add_separator()
    menuPlik.add_command(label="Zakończ", command=zakoncz)

    menuEdycja = Menu(pasekMenu, tearoff=0)
    pasekMenu.add_cascade(label="Edycja", menu=menuEdycja)

    menuEdycja.add_command(label="Cofnij", command=cofnij)

    menuHelp = Menu(pasekMenu, tearoff=0)
    pasekMenu.add_cascade(label="Pomoc", menu=menuHelp)

    menuHelp.add_command(label="Pomoc", command=pomoc)
    menuHelp.add_separator()
    menuHelp.add_command(label="O aplikacji...", command=oaplikacji)

    Aplikacja.config(menu=pasekMenu)

    przygotujPlansze()

    Aplikacja.mainloop()

def czyscPlansze():
    global przyciski
    global obecnyGracz
    global ostatniRuch

    for przycisk in przyciski:
        przycisk['text'] = ''
    obecnyGracz = 'X'
    ostatniRuch = -1

def sprawdzZwyciestwoNaIndeksach(i1, i2, i3):
    global przyciski

    return przyciski[i1]['text'] != '' and przyciski[i1]['text'] == przyciski[i2]['text'] == przyciski[i3]['text']

def sprawdzZwyciestwo():
    global przyciski

    return sprawdzZwyciestwoNaIndeksach(0, 1, 2) or \
           sprawdzZwyciestwoNaIndeksach(3, 4, 5) or \
           sprawdzZwyciestwoNaIndeksach(6, 7, 8) or \
           sprawdzZwyciestwoNaIndeksach(0, 3, 6) or \
           sprawdzZwyciestwoNaIndeksach(1, 4, 7) or \
           sprawdzZwyciestwoNaIndeksach(2, 5, 8) or \
           sprawdzZwyciestwoNaIndeksach(0, 4, 8) or \
           sprawdzZwyciestwoNaIndeksach(2, 4, 6)

def zmianaGracza():
    global obecnyGracz

    if (obecnyGracz == 'X'):
        obecnyGracz = 'O'
    else:
        obecnyGracz = 'X'

def buttonClick(index):
    global przyciski
    global obecnyGracz
    global ostatniRuch

    if przyciski[index]['text'] != '':
        return

    przyciski[index]['text'] = obecnyGracz
    ostatniRuch = index

    if sprawdzZwyciestwo():
        messagebox.showinfo("Wygrana!", "Wygrał gracz " + obecnyGracz + "!")
        czyscPlansze()
        return

    zmianaGracza()

def przygotujPlansze():
    global przyciski
    global obecnyGracz

    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(0)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(1)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(2)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(3)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(4)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(5)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(6)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(7)))
    przyciski.append(Button(height = 5, width = 10, text = '', command = lambda: buttonClick(8)))

    id = 0
    for i in range(1, 4):
        for j in range(1, 4):
            przyciski[id].place(x = 10 + 90 * (i - 1), y = 10 + 95 * (j - 1))
            id += 1

def main():
    przygotujOkno()

main()
    
