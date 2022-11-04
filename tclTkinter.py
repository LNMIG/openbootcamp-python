import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="Hola", bg="yellow", fg="blue")
label_saludo.pack(ipadx=50, ipady=50, expand=True)

label_adios = tkinter.Label(window, text="Adios", bg="red", fg="white")
label_adios.pack(fill="both", expand=True)


window.mainloop()