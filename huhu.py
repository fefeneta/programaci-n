import tkinter as tk

def mostrarOpcion1():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 1", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion2():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 2", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)
    
def mostrarOpcion3():
    limpiarVentana()
    label = tk.Label(ventana, text= "Elegiste la Opción 3", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion4():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 4", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def limpiarVentana():  
    for widget in ventana.winfo_children():  
        widget.destroy()

        
def mostrarMenu():
    limpiarVentana()
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Opción 1", font=("Arial", 14), width=20, command=mostrarOpcion1)
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text="Opción 2", font=("Arial", 14), width=20, command=mostrarOpcion2)
    boton2.pack(pady=10)
    
    boton3 = tk.Button(ventana, text="Opción 3", font=("Arial", 14), width=20, command=mostrarOpcion3)
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana, text="Opción 4", font=("Arial", 14), width=20, command=mostrarOpcion4)
    boton4.pack(pady=10)

def main():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("400x300")
    ventana.title("Menú Centrado")

    mostrarMenu()

    ventana.mainloop()

if __name__=="__main__":
    main()
