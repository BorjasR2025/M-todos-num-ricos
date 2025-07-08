import tkinter as tk
from tkinter import messagebox
import numpy as np

def secante(f, x0, x1, tol, max_iter=100):
    """Implementa el método de la secante."""
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            raise ZeroDivisionError("División por cero en el método de la secante.")

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tol:
            return x2, i

        x0, x1 = x1, x2

    raise RuntimeError("Máximo de iteraciones alcanzado sin encontrar raíz.")

def ejecutar_secante():
    """Obtiene parámetros de la GUI, resuelve y muestra resultado."""
    try:
        func_str = func_entry.get()
        a = float(a_entry.get()) 
        b = float(b_entry.get()) 
        tol = float(tol_entry.get()) 
        
        f = lambda x: eval(func_str, {"np": np, "x": x})  # Carga la expresión
        
        raiz, iteraciones = secante(f, a, b, tol)
        messagebox.showinfo("Resultado", f"La raíz aproximada es {raiz}\nIteraciones: {iteraciones}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Creamos la GUI
root = tk.Tk()
root.title("Método de la Secante")
root.geometry("400x500")
root.config(bg="#edf2f4")

frame = tk.Frame(root, bg="#edf2f4")
frame.pack(pady=20)

titulo = tk.Label(frame, text="Secante de Funciones", font=('Helvetica', 16, 'bold'), bg="#edf2f4")
titulo.grid(row=0, columnspan=2, pady=10)

instruccion = tk.Label(frame, text='Ingrese f(x) en Python (ejemplo: x**3 - x - 2)', font=('Helvetica', 11), bg="#edf2f4")
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

calcular = tk.Button(frame, text="Calcular Raíz", font=('Helvetica', 11, 'bold'), command=ejecutar_secante, bg="#0939da")
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
