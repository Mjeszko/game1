import tkinter

class KolkoKrzyzyk(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

KKapka= KolkoKrzyzyk()

KKapka.master.title("Kó³ko i krzy¿yk")
KKapka.master.geometry("400x400")

KKapka.mainloop()
