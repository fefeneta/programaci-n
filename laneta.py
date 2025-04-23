import tkinter as tk
def main() :
    ventana = tk.Tk ()
    ventana.title ("ejercicio 2")
    ventana.geometry("700x700")
    ventana.configure(bg="lightblue")
    
    etiqueta = tk.Label(ventana, text="ejercicio 2", font=("arial", 16))
    etiqueta.pack()
    etiqueta = tk.Label(ventana, text="federico", font=("arial", 16))
    etiqueta.pack()
    ventana.mainloop()

if __name__=="__main__":
    main()
