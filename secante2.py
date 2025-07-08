import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from stylesecante2 import aplicar_estilo  # Asegúrate que exista y contenga la función aplicar_estilo

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

    raise RuntimeError("Se alcanzó el número máximo de iteraciones.")

def ejecutar_secante():
    try:
        func_str = func_entry.get()
        a = float(a_entry.get())
        b = float(b_entry.get())
        tol = float(tol_entry.get())
        # Evalúa usando solo numpy y x
        f = lambda x: eval(func_str, {"__builtins__": None, "np": np, "x": x})
        raiz, iteraciones = secante(f, a, b, tol)
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
root.title("Método de la Secante")
root.geometry("900x600")

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Entradas a la izquierda
input_frame = tk.Frame(main_frame)
input_frame.pack(side='left', fill='y', padx=10)

tk.Label(input_frame, text="Secante de Funciones").grid(row=0, columnspan=2, pady=10)
tk.Label(input_frame, text="f(x):").grid(row=1, column=0, sticky='e', pady=5)
func_entry = tk.Entry(input_frame, width=30)
func_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="a (x0):").grid(row=2, column=0, sticky='e', pady=5)
a_entry = tk.Entry(input_frame, width=30)
a_entry.grid(row=2, column=1, pady=5)

tk.Label(input_frame, text="b (x1):").grid(row=3, column=0, sticky='e', pady=5)
b_entry = tk.Entry(input_frame, width=30)
b_entry.grid(row=3, column=1, pady=5)

tk.Label(input_frame, text="Tolerancia:").grid(row=4, column=0, sticky='e', pady=5)
tol_entry = tk.Entry(input_frame, width=30)
tol_entry.grid(row=4, column=1, pady=5)

tk.Button(input_frame, text="Calcular Raíz", command=ejecutar_secante).grid(row=5, columnspan=2, pady=10)

# Ayuda
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

# Aplicar estilo
aplicar_estilo(root)

root.mainloop()
