import tkinter as tk
from tkinter import messagebox
import numpy as np

def biseccion(f, a, b, tol, max_iter=100):
    """Implementa el método de bisección."""
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) y f(b) tienen el MISMO signo.")
    
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c, i

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    raise RuntimeError("Máximo de iteraciones alcanzado sin encontrar raíz.")
    

def ejecutar_biseccion():
    """Obtiene parámetros de la GUI, resuelve y muestra resultado."""
    try:
        func_str = func_entry.get()
        a = float(a_entry.get()) 
        b = float(b_entry.get()) 
        tol = float(tol_entry.get()) 
        
        f = lambda x: eval(func_str, {"np":np,"x":x})  # Carga la expresión de forma segura
    
        raiz, iteraciones = biseccion(f, a, b, tol)
        messagebox.showinfo("Resultado", f"La raíz aproximada es {raiz}\nIteraciones: {iteraciones}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Creamos la GUI
root = tk.Tk()
root.title("Método de Bisección")
root.geometry("400x500")
root.config(bg="#edf2f4")

frame = tk.Frame(root, bg="#edf2f4")
frame.pack(pady=20)

titulo = tk.Label(frame, text="Bisección de Funciones", font=('Helvetica', 16, 'bold'), bg="#edf2f4")
titulo.grid(row=0, columnspan=2, pady=10)

instruccion = tk.Label(frame, text='Ingrese una f(x) ', font=('Helvetica', 11), bg="#edf2f4")
instruccion.grid(row=1, columnspan=2, pady=5)

tk.Label(frame, text="f(x):", font=('Helvetica', 11), bg="#edf2f4").grid(row=2, column=0, sticky='e', pady=5)
func_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
func_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Valor de a :", font=('Helvetica', 11), bg="#edf2f4").grid(row=3, column=0, sticky='e', pady=5)
a_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
a_entry.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Valor de b :", font=('Helvetica', 11), bg="#edf2f4").grid(row=4, column=0, sticky='e', pady=5)
b_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
b_entry.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Tolerancia :", font=('Helvetica', 11), bg="#edf2f4").grid(row=5, column=0, sticky='e', pady=5)
tol_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
tol_entry.grid(row=5, column=1, pady=5)

calcular = tk.Button(frame, text="Calcular Raíz", font=('Helvetica', 11, 'bold'), command=ejecutar_biseccion, bg="#0939da")
calcular.grid(row=6, columnspan=2, pady=20)

# Marco con información de funciones
marco = tk.Frame(root, bd=2, relief='solid', bg="#edf2f4")
marco.pack(side='bottom', fill='x', pady=10, padx=10)

titulo_marco = tk.Label(marco, text="Ejemplos de Funciones y Uso", font=('Helvetica', 13, 'bold'), bg="#edf2f4")
titulo_marco.pack(pady=5)

descripcion = """Puedes usar:
- np.sin(x)  → Funciones trigonométricas
- np.exp(x)  → Funciones exponenciales
- np.log(x)  → Logaritmo natural
- x**2       → Elevar al cuadrado
- x**3 - x - 2 → Polinomio cúbico

Consejo: Siempre utiliza 'np.' antes de sin, exp, log, etc."""  

label_descripcion = tk.Label(marco, text=descripcion, font=('Helvetica', 10), bg="#edf2f4", justify='left')
label_descripcion.pack(pady=5)

root.mainloop()
