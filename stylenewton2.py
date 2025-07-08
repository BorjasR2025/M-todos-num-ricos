def aplicar_estilo(root):
    """Aplica estilos generales al fondo y recorre todos los widgets."""
    root.config(bg="#edf2f4")
    for widget in root.winfo_children():
        aplicar_recursivo(widget)

def aplicar_recursivo(widget):
    clase = widget.winfo_class()
    opciones = widget.configure()

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
            widget.config(bg="#0a1172")
        if "activebackground" in opciones:
            widget.config(activebackground="#5eb1bf")

    for child in widget.winfo_children():
        aplicar_recursivo(child)
