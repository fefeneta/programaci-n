import tkinter as tk  
from urllib.request import urlopen  
from PIL import Image, ImageTk  
from io import BytesIO  

def descargarImagenPortada():
    urlImagen = "data:image/png;base64,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"
    datosImagen = urlopen(urlImagen)
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarImagenFondo():
    urlImagen = "https://github.com/fefeneta/imagenes/blob/main/portada.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarImagenCapsulas():
    urlImagen = "https://github.com/fefeneta/imagenes/blob/main/cafetera-nespresso-inissia-red-07l-19bares-roja-14276.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarImagenItaliana():
    urlImagen = "https://github.com/fefeneta/imagenes/blob/main/cafetera-nespresso-inissia-red-07l-19bares-roja-14276.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarImagenExpresso():
    urlImagen = "https://github.com/fefeneta/imagenes/blob/main/cafetera-nespresso-inissia-red-07l-19bares-roja-14276.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen


def descargarImagenChemex():
    urlImagen = "https://github.com/fefeneta/imagenes/blob/main/cafetera-nespresso-inissia-red-07l-19bares-roja-14276.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def mostrarCapsulas():
    limpiarVentana()
    etiqueta = tk.Label(ventana, image=ventana.capsula)
    etiqueta.place(width=ancho, height=alto)
    
    label = tk.Label(ventana, text="Elegiste la Cafetera de capsulas", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarItaliana():
    limpiarVentana()
    etiqueta = tk.Label(ventana, image=ventana.fondo)
    etiqueta.place(width=ancho, height=alto)
    
    etiqueta = tk.Label(ventana, image=ventana.capsula)
    etiqueta.place(width=ancho, height=alto)
    
    label = tk.Label(ventana, text="Elegiste la Cafetera italiana", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)
    
def mostrarExpresso():
    limpiarVentana()
    etiqueta = tk.Label(ventana, image=ventana.fondo)
    etiqueta.place(width=ancho, height=alto)
    
    etiqueta = tk.Label(ventana, image=ventana.capsula)
    etiqueta.place(width=ancho, height=alto)
    label = tk.Label(ventana, text= "Elegiste la Cafetera de expresso", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarChemex():
    limpiarVentana()
    etiqueta = tk.Label(ventana, image=ventana.fondo)
    etiqueta.place(width=ancho, height=alto)
    
    etiqueta = tk.Label(ventana, image=ventana.capsula)
    etiqueta.place(x=500, y=100, width=300, height=400)
    label = tk.Label(ventana, text="Elegiste la Cafetera chemex", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def limpiarVentana():  
    for widget in ventana.winfo_children():  
        widget.destroy()

        
def mostrarMenu():
    limpiarVentana()
    etiqueta = tk.Label(ventana, image=ventana.fondo)
    etiqueta.place(width=ancho, height=alto) 
    
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Cafetera de capsulas", font=("Arial", 14), width=20, command=mostrarCapsulas)
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text= "Cafetera italiana", font=("Arial", 14), width=20, command=mostrarItaliana)
    boton2.pack(pady=10)
    
    boton3 = tk.Button(ventana, text="Cafetera de expresso", font=("Arial", 14), width=20, command=mostrarExpresso)
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana, text="Cafetera chemex", font=("Arial", 14), width=20, command=mostrarChemex)
    boton4.pack(pady=10)

def main():
    global ventana
    global alto
    global ancho 
    ventana = tk.Tk()
    
    ventana.title("Menú Centrado")
    ancho = ventana.winfo_screenwidth() 
    alto = ventana.winfo_screenheight()  
    ventana.geometry(f"{ancho}x{alto}")

    imagen=descargarImagenPortada()
    imagenRedimensionada = imagen.resize((ancho, alto),Image.Resampling.LANCZOS)
    portadaTk = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.portada=portadaTk
    etiqueta = tk.Label(ventana, image=ventana.portada)
    etiqueta.place(width=ancho, height=alto)
   

    imagen=descargarImagenFondo()
    imagenRedimensionada = imagen.resize((ancho, alto),Image.Resampling.LANCZOS)
    fondoTk = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.fondo=fondoTk
   

    imagen=descargarImagenCapsulas()
    imagenRedimensionada = imagen.resize((ancho, alto),Image.Resampling.LANCZOS)
    capsulaTk = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.capsula=capsulaTk
    etiqueta = tk.Label(ventana, image=ventana.capsula)
    etiqueta.place(width=ancho, height=alto)
    
    imagen=descargarImagenItaliana()
    imagenRedimensionada = imagen.resize((ancho, alto),Image.Resampling.LANCZOS)
    italianaTk = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.italiana=italianaTk
    etiqueta = tk.Label(ventana, image=ventana.italiana)
    etiqueta.place(width=ancho, height=alto)


    imagen=descargarImagenExpresso()
    imagenRedimensionada = imagen.resize((ancho, alto),Image.Resampling.LANCZOS)
    italianaTk = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.italiana=italianaTk
    etiqueta = tk.Label(ventana, image=ventana.italiana)
    etiqueta.place(width=ancho, height=alto)

    imagen=descargarImagenChemex()
    imagenRedimensionada = imagen.resize((ancho, alto),Image.Resampling.LANCZOS)
    chemexTk = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.chemex=chemexTk
    etiqueta = tk.Label(ventana, image=ventana.chemex)
    etiqueta.place(width=ancho, height=alto)

    

    boton5 = tk.Button(ventana, text="Inicio", font=("Arial", 14), width=20, command=mostrarMenu)
    boton5.pack(pady=10)
    
    ventana.mainloop()

if __name__=="__main__":
    main()
   
    
