import tkinter
from tkinter import *
from tkinter import ttk
from GetData import GetData
import threading 
class Interface():
    def execute(self):
        window = Tk()
        window.title("Calculadora de Rota")
        window.geometry("500x500+100+0")

        self.text_distancia = Label(window, text="0")
        self.text_distancia.pack()

        button_buscar = ttk.Button(window,text="Buscar",command=lambda: threading.Thread(target=self.get).start())
        button_buscar.pack()

        button_visualizar = ttk.Button(window, text="Visualizar")
        button_visualizar.pack()
        mainloop()

    def get(self, fromCity, toCity):
        fromCit =  "São paulo, SP"
        toCity = "Rua alegrete, 118, jardim gonçalves"
        distancia = GetData().get(fromCity, toCity)
        self.text_distancia.config(text=distancia)

Interface().execute()