import tkinter as tk
from tkinter import messagebox
import numpy as np

def newton_raphson(f, df, x0, tol, max_iter=100):
    """Implementa el método de Newton-Raphson."""
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        df_x0 = df(x0)
        if df_x0 == 0:
            raise ZeroDivisionError("Derivada cero. Método no puede continuar.")

        x1 = x0 - f_x0 / df_x0

        if abs(x1 - x0) < tol:
            return x1, i

        x0 = x1

    raise RuntimeError("Máximo de iteraciones alcanzado sin encontrar raíz.")

def ejecutar_newton():
    """Obtiene parámetros de la GUI, ejecuta Newton-Raphson y muestra resultado."""
    try:
        func_str = func_entry.get()
        deriv_str = deriv_entry.get()
        x0 = float(x0_entry.get())
        tol = float(tol_entry.get())
        
        f = lambda x: eval(func_str, {"np": np, "x": x})
        df = lambda x: eval(deriv_str, {"np": np, "x": x})

        raiz, iteraciones = newton_raphson(f, df, x0, tol)
        messagebox.showinfo("Resultado", f"La raíz aproximada es {raiz}\nIteraciones: {iteraciones}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Método de Newton-Raphson")
root.geometry("420x540")
root.config(bg="#edf2f4")

frame = tk.Frame(root, bg="#edf2f4")
frame.pack(pady=20)

titulo = tk.Label(frame, text="Newton-Raphson para Raíces", font=('Helvetica', 16, 'bold'), bg="#edf2f4")
titulo.grid(row=0, columnspan=2, pady=10)

instruccion = tk.Label(frame, text='Ingrese f(x) y su derivada usando\nEjemplo: x**3 - x - 2  y  3*x**2 - 1', font=('Helvetica', 11), bg="#edf2f4")
instruccion.grid(row=1, columnspan=2, pady=5)

tk.Label(frame, text="f(x):", font=('Helvetica', 11), bg="#edf2f4").grid(row=2, column=0, sticky='e', pady=5)
func_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
func_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="f'(x):", font=('Helvetica', 11), bg="#edf2f4").grid(row=3, column=0, sticky='e', pady=5)
deriv_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
deriv_entry.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Valor inicial x0:", font=('Helvetica', 11), bg="#edf2f4").grid(row=4, column=0, sticky='e', pady=5)
x0_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
x0_entry.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Tolerancia:", font=('Helvetica', 11), bg="#edf2f4").grid(row=5, column=0, sticky='e', pady=5)
tol_entry = tk.Entry(frame, width=30, font=('Helvetica', 11))
tol_entry.grid(row=5, column=1, pady=5)

calcular = tk.Button(frame, text="Calcular Raíz", font=('Helvetica', 11, 'bold'), command=ejecutar_newton, bg="#0939da", fg="white")
calcular.grid(row=6, columnspan=2, pady=20)

# Marco inferior con ayuda
marco = tk.Frame(root, bd=2, relief='solid', bg="#edf2f4")
marco.pack(side='bottom', fill='x', pady=10, padx=10)

titulo_marco = tk.Label(marco, text="Ejemplos de Funciones y Uso", font=('Helvetica', 13, 'bold'), bg="#edf2f4")
titulo_marco.pack(pady=5)

descripcion = """Puedes usar:
- np.sin(x)     → Seno
- np.exp(x)     → Exponencial
- np.log(x)     → Logaritmo natural
- x**2          → Cuadrado
- x**3 - x - 2  → Polinomio cúbico

Recuerda usar 'np.' para funciones matemáticas de numpy."""
label_descripcion = tk.Label(marco, text=descripcion, font=('Helvetica', 10), bg="#edf2f4", justify='left')
label_descripcion.pack(pady=5)

root.mainloop()
