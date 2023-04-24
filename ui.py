import time
import tkinter
import customtkinter
import main
import os
import database




def Data_Command():
    Data = database.DataCollector()
    Data.create_database()
    create_database.destroy()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry('750x500')
app.resizable(0,0)
app.title("Energi Monitor")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill="both", expand=True)

create_database = customtkinter.CTkButton(master=frame, text="Create DataBase", command=Data_Command)
create_database.place(relx=0.75, rely=0.9)


power = main.power_collector()
total = main.total_collector()




def ui():
    
    
    
    title = customtkinter.CTkLabel(master=frame, text="Energi Monitor")
    title.configure(font=('Microsoft YaHei UI Light', 24))
    title.place(relx=0.38, rely=0.01)
    
    
    
    price_label = customtkinter.CTkLabel(master=frame, text=f"Kw/t pris: {main.price_getter()} kr")
    price_label.configure(font=('Microsoft YaHei UI Light', 24))
    price_label.place(relx=0.02, rely=0.4)
    
    
    power_label = customtkinter.CTkLabel(master=frame, text=f"Nuværende forbrug: {power}")
    power_label.configure(font=('Microsoft YaHei UI Light', 16))
    power_label.place(relx=0.02, rely=0.6)
    
    
    total_label = customtkinter.CTkLabel(master=frame, text=f"Totalt forbrug: {total}")
    total_label.configure(font=('Microsoft YaHei UI Light', 16))
    total_label.place(relx=0.02, rely=0.65)
    
    price_label = customtkinter.CTkLabel(master=frame, text=f"Pris: {total} kr")
    price_label.configure(font=('Microsoft YaHei UI Light', 16))
    price_label.place(relx=0.02, rely=0.72)
    
    
    energy_box = customtkinter.CTkCheckBox(master=frame, text="Update Data")
    energy_box.place(relx=0.025, rely=0.91)
    
    
    try:
        if os.path.exists('data.db'):
            create_database.destroy()
    except Exception as err:
        print(f"Error: {err}")
    
    
    app.mainloop()
    
    
    
