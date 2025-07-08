import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from stylenewton2 import aplicar_estilo  # Asegúrate que el nombre sea correcto

def newton_raphson(f, df, x0, tol, max_iter=100):
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ZeroDivisionError("La derivada se anuló. El método no puede continuar.")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1, i
        x0 = x1
    raise RuntimeError("Se alcanzó el número máximo de iteraciones.")

def ejecutar_newton():
    try:
        func_str = func_entry.get()
        deriv_str = deriv_entry.get()
        x0 = float(x0_entry.get())
        tol = float(tol_entry.get())

        f = lambda x: eval(func_str, {"__builtins__": None, "np": np, "x": x})
        df = lambda x: eval(deriv_str, {"__builtins__": None, "np": np, "x": x})

        raiz, iteraciones = newton_raphson(f, df, x0, tol)
        messagebox.showinfo("Resultado", f"La raíz aproximada es {raiz:.6f}\nIteraciones: {iteraciones}")
        graficar_funcion(f, raiz)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def graficar_funcion(f, x0):
    x_vals = np.linspace(x0 - 5, x0 + 5, 400)
    try:
        y_vals = [f(x) for x in x_vals]
    except:
        messagebox.showerror("Error", "No se pudo graficar la función.")
        return

    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(x_vals, y_vals, label='f(x)', color='blue')
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(x0, color='green', linestyle=':', label="Raíz aproximada")
    ax.set_title("Gráfica de f(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()
    canvas.draw()

# ---------- GUI PRINCIPAL ----------
root = tk.Tk()
root.title("Método de Newton-Raphson")
root.geometry("900x600")

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Entradas a la izquierda
input_frame = tk.Frame(main_frame)
input_frame.pack(side='left', fill='y', padx=10)

tk.Label(input_frame, text="Newton-Raphson").grid(row=0, columnspan=2, pady=10)
tk.Label(input_frame, text="f(x):").grid(row=1, column=0, sticky='e', pady=5)
func_entry = tk.Entry(input_frame, width=30)
func_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="f'(x):").grid(row=2, column=0, sticky='e', pady=5)
deriv_entry = tk.Entry(input_frame, width=30)
deriv_entry.grid(row=2, column=1, pady=5)

tk.Label(input_frame, text="x₀:").grid(row=3, column=0, sticky='e', pady=5)
x0_entry = tk.Entry(input_frame, width=30)
x0_entry.grid(row=3, column=1, pady=5)

tk.Label(input_frame, text="Tolerancia:").grid(row=4, column=0, sticky='e', pady=5)
tol_entry = tk.Entry(input_frame, width=30)
tol_entry.grid(row=4, column=1, pady=5)

tk.Button(input_frame, text="Calcular Raíz", command=ejecutar_newton).grid(row=5, columnspan=2, pady=10)

ayuda_frame = tk.Frame(input_frame, bd=1, relief='solid')
ayuda_frame.grid(row=6, columnspan=2, pady=15, sticky='ew')
tk.Label(
    ayuda_frame,
    text="""Puedes usar:
- np.sin(x)  → Funciones trigonométricas
- np.exp(x)  → Funciones exponenciales
- np.log(x)  → Logaritmo natural
- x**2       → Potencias
- Recuerda incluir f'(x)

Ejemplo:
f(x) = x**3 - x - 2
f'(x) = 3*x**2 - 1"""
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
