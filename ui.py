import main
from tkinter import *
import customtkinter as frame
import db


def UI():
    pris = main.price()

    frame.set_appearance_mode("Dark")
    frame.set_default_color_theme("blue")

    app = frame.CTk()
    app.geometry('750x500')
    app.resizable(0,0)
    app.title("Energi Måler")


    nuværende_el_pris = frame.CTkLabel(app, text=f'Nuværende Kw/t pris: {pris} Kr')
    nuværende_el_pris.configure(font=('Microsoft YaHei UI Light', 16))
    nuværende_el_pris.place(x=10, y= 10)


    creation_data = db.DataInsertion()
    

    data_knap = frame.CTkButton(master=app, text="Create Database", command=creation_data.create_data())
    data_knap.place(relx=0.8, rely= 0.92)

    data_knap = frame.CTkCheckBox(master=app, text="Update Data")
    data_knap.place(relx=0.8, rely= 0.85)     


    
    app.mainloop()

