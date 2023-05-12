import tkinter
from tkinter import *
from tkinter import ttk
from GetData import GetData
class Interface():
    def execute(self):
        window = Tk()
        window.title("Calculadora de Rota")
        window.geometry("500x500+100+0")

        self.text_distancia = Label(window, text="0")
        self.text_distancia.pack()

        button_buscar = ttk.Button(window,text="Buscar",command=lambda: self.get("São paulo, SP", "Rua alegrete, 118, jardim gonçalves"))
        button_buscar.pack()

        button_visualizar = ttk.Button(window, text="Visualizar")
        button_visualizar.pack()
        mainloop()

    def get(self, fromCity, toCity):
        distancia = GetData().get(fromCity, toCity)
        self.text_distancia.config(text=distancia)

Interface().execute()