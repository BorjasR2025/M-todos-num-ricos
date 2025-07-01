import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from stylebiseccion2 import aplicar_estilo  # Asegúrate de que esté en el mismo folder

def biseccion(f, a, b, tol, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos.")

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
    raise RuntimeError("Se alcanzó el número máximo de iteraciones.")

def ejecutar_biseccion():
    try:
        func_str = func_entry.get()
        a = float(a_entry.get())
        b = float(b_entry.get())
        tol = float(tol_entry.get())
        f = lambda x: eval(func_str, {"__builtins__": None, "np": np, "x": x})
        raiz, iteraciones = biseccion(f, a, b, tol)
        messagebox.showinfo("Resultado", f"La raíz aproximada es {raiz:.6f}\nIteraciones: {iteraciones}")
        graficar_funcion(f, a, b)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def graficar_funcion(f, a, b):
    x_vals = np.linspace(a, b, 400)
    try:
        y_vals = [f(x) for x in x_vals]
    except:
        messagebox.showerror("Error", "No se pudo graficar la función.")
        return

    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(x_vals, y_vals, label='f(x)', color='blue')
    ax.axhline(0, color='black', linestyle='--')
    ax.set_title("Gráfica de f(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()
    canvas.draw()

# ---------- GUI PRINCIPAL ----------
root = tk.Tk()
root.title("Método de Bisección")
root.geometry("900x600")

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Entradas a la izquierda
input_frame = tk.Frame(main_frame)
input_frame.pack(side='left', fill='y', padx=10)

tk.Label(input_frame, text="Bisección de Funciones").grid(row=0, columnspan=2, pady=10)
tk.Label(input_frame, text="f(x):").grid(row=1, column=0, sticky='e', pady=5)
func_entry = tk.Entry(input_frame, width=30)
func_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="a:").grid(row=2, column=0, sticky='e', pady=5)
a_entry = tk.Entry(input_frame, width=30)
a_entry.grid(row=2, column=1, pady=5)

tk.Label(input_frame, text="b:").grid(row=3, column=0, sticky='e', pady=5)
b_entry = tk.Entry(input_frame, width=30)
b_entry.grid(row=3, column=1, pady=5)

tk.Label(input_frame, text="Tolerancia:").grid(row=4, column=0, sticky='e', pady=5)
tol_entry = tk.Entry(input_frame, width=30)
tol_entry.grid(row=4, column=1, pady=5)

tk.Button(input_frame, text="Calcular Raíz", command=ejecutar_biseccion).grid(row=5, columnspan=2, pady=10)

ayuda_frame = tk.Frame(input_frame, bd=1, relief='solid')
ayuda_frame.grid(row=6, columnspan=2, pady=15, sticky='ew')
tk.Label(
    ayuda_frame,
    text="""Puedes usar:
- np.sin(x)  → Funciones trigonométricas
- np.exp(x)  → Funciones exponenciales
- np.log(x)  → Logaritmo natural
- x**2       → Elevar al cuadrado
- x**3 - x - 2 → Polinomio cúbico

Consejo: Siempre utiliza 'np.' antes de sin, exp, log, etc."""
).pack(padx=10, pady=5)

# Gráfico a la derecha
grafica_frame = tk.Frame(main_frame, bd=2, relief='groove')
grafica_frame.pack(side='right', fill='both', expand=True, padx=10)

fig = plt.Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=grafica_frame)
canvas.get_tk_widget().pack(fill='both', expand=True)

# Aplicar estilo sin errores
aplicar_estilo(root)

root.mainloop()
