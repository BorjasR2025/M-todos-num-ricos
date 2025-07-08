def aplicar_estilo(root):
    """Aplica estilos generales al fondo y recorre todos los widgets."""
    root.config(bg="#edf2f4")
    for widget in root.winfo_children():
        aplicar_recursivo(widget)

def aplicar_recursivo(widget):
    """Aplica estilos solo si el widget lo soporta, evitando errores."""
    clase = widget.winfo_class()
    try:
        opciones = widget.configure()
    except Exception:
        opciones = {}

    if "bg" in opciones:
        widget.config(bg="#edf2f4")
    if "font" in opciones:
        widget.config(font=('Helvetica', 11))
    if clase == "Label" and "fg" in opciones:
        widget.config(fg="#333")
    elif clase == "Button":
        if "fg" in opciones:
            widget.config(fg="#fff")
        if "bg" in opciones:
            widget.config(bg="#0210a9")
        if "activebackground" in opciones:
            widget.config(activebackground="#00c1e3")
    elif clase == "Entry":
        if "bg" in opciones:
            widget.config(bg="white")
        if "fg" in opciones:
            widget.config(fg="#333")

    for child in widget.winfo_children():
        aplicar_recursivo(child)
