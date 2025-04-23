import tkinter as tk
def main() :
    ventana = tk.Tk ()
    ventana.title ("ejercicio 2")
    ventana.geometry("700x700")
    ventana.configure(bg="lightblue")
    etiqueta1 = tk.Label(ventana, text="ejercicio 2", font=("arial", 16))
    etiqueta1.pack()
    etiqueta2 = tk.Label(ventana, text="Ingrese su nombre:", font=("arial", 16))
    etiqueta2.pack()
    campo=tk.Entry (ventana)
    campo.pack()
    
    
    def saludar():
        nombre=campo.get()
        etiqueta3 = tk.Label(ventana, text=f"hola {nombre}, te saluda fede", font=("arial", 16))
        etiqueta3.pack()
        
    boton1 = tk.Button(ventana, text="saludar", command=saludar)
    boton1.pack (pady=5)

   
    
    
    ventana.mainloop()

if __name__=="__main__":
    main()
