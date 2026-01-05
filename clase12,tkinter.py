import tkinter as tk
from tkinter import ttk

# -------------------------
# CLASES DE LÓGICA
# -------------------------
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible."

    def devolver(self):
        self.disponible = True
        return f"El libro '{self.titulo}' ha sido devuelto."


class Prestamo:
    def __init__(self, libro, fecha_prestamo):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False

    def marcar_devolucion(self):
        self.devuelto = True
        return self.libro.devolver()


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def realizar_prestamo(self, libro, fecha):
        if libro.disponible:
            libro.prestar()
            nuevo_prestamo = Prestamo(libro, fecha)
            self.prestamos.append(nuevo_prestamo)
            return f"✅ Préstamo realizado: {libro.titulo} ({fecha})"
        else:
            return f"❌ El libro '{libro.titulo}' no está disponible."

    def mostrar_prestamos(self):
        info = []
        for p in self.prestamos:
            estado = "Devuelto" if p.devuelto else "Pendiente"
            info.append(f"{p.libro.titulo} - {estado} ({p.fecha_prestamo})")
        return "\n".join(info) if info else "Sin préstamos."


# -------------------------
# INTERFAZ TKINTER
# -------------------------
class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Sistema de Biblioteca")
        self.root.geometry("650x520")
        self.root.config(bg="#D6EAF8")  # Fondo general azul claro

        # Personalización de estilo ttk
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#D6EAF8", foreground="#1B2631", font=("Arial", 10))
        style.configure("TButton", background="#5DADE2", foreground="black", font=("Arial", 10, "bold"))
        style.map("TButton", background=[("active", "#3498DB")])
        style.configure("TFrame", background="#D6EAF8")

        # Listas para objetos
        self.libros = []
        self.usuarios = []

        # Variables
        self.titulo_var = tk.StringVar()
        self.autor_var = tk.StringVar()
        self.isbn_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.id_var = tk.StringVar()
        self.fecha_var = tk.StringVar()

        self.crear_interfaz()

    def crear_interfaz(self):
        ttk.Label(self.root, text="📖 SISTEMA DE BIBLIOTECA", font=("Arial", 16, "bold"), background="#AED6F1").pack(pady=10, fill="x")

        frame = ttk.Notebook(self.root)
        frame.pack(expand=True, fill="both")

        self.tab_libros = ttk.Frame(frame)
        self.tab_usuarios = ttk.Frame(frame)
        self.tab_prestamos = ttk.Frame(frame)

        frame.add(self.tab_libros, text="Registrar Libros")
        frame.add(self.tab_usuarios, text="Registrar Usuarios")
        frame.add(self.tab_prestamos, text="Préstamos")

        self.interfaz_libros()
        self.interfaz_usuarios()
        self.interfaz_prestamos()

    # --- Libros ---
    def interfaz_libros(self):
        ttk.Label(self.tab_libros, text="Título:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.tab_libros, textvariable=self.titulo_var).grid(row=0, column=1, padx=5)

        ttk.Label(self.tab_libros, text="Autor:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.tab_libros, textvariable=self.autor_var).grid(row=1, column=1, padx=5)

        ttk.Label(self.tab_libros, text="ISBN:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.tab_libros, textvariable=self.isbn_var).grid(row=2, column=1, padx=5)

        ttk.Button(self.tab_libros, text="Agregar Libro", command=self.agregar_libro).grid(row=3, column=0, columnspan=2, pady=10)

        self.lista_libros = tk.Listbox(self.tab_libros, width=50, bg="#EBF5FB", fg="#1B2631", relief="flat")
        self.lista_libros.grid(row=4, column=0, columnspan=2, pady=10)

        self.lbl_result_libros = tk.Label(self.tab_libros, text="", bg="#EBF5FB", fg="#1B2631", width=60, height=3, anchor="nw", justify="left", relief="groove")
        self.lbl_result_libros.grid(row=5, column=0, columnspan=2, pady=10)

    def agregar_libro(self):
        titulo = self.titulo_var.get()
        autor = self.autor_var.get()
        isbn = self.isbn_var.get()
        if titulo and autor and isbn:
            libro = Libro(titulo, autor, isbn)
            self.libros.append(libro)
            self.lista_libros.insert(tk.END, f"{titulo} - {autor}")
            self.titulo_var.set("")
            self.autor_var.set("")
            self.isbn_var.set("")
            self.lbl_result_libros.config(text="✅ Libro agregado correctamente.")
        else:
            self.lbl_result_libros.config(text="⚠️ Complete todos los campos.")

    # --- Usuarios ---
    def interfaz_usuarios(self):
        ttk.Label(self.tab_usuarios, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.tab_usuarios, textvariable=self.nombre_var).grid(row=0, column=1, padx=5)

        ttk.Label(self.tab_usuarios, text="ID Usuario:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.tab_usuarios, textvariable=self.id_var).grid(row=1, column=1, padx=5)

        ttk.Button(self.tab_usuarios, text="Registrar Usuario", command=self.agregar_usuario).grid(row=2, column=0, columnspan=2, pady=10)

        self.lista_usuarios = tk.Listbox(self.tab_usuarios, width=50, bg="#EBF5FB", fg="#1B2631", relief="flat")
        self.lista_usuarios.grid(row=3, column=0, columnspan=2, pady=10)

        self.lbl_result_usuarios = tk.Label(self.tab_usuarios, text="", bg="#EBF5FB", fg="#1B2631", width=60, height=3, anchor="nw", justify="left", relief="groove")
        self.lbl_result_usuarios.grid(row=4, column=0, columnspan=2, pady=10)

    def agregar_usuario(self):
        nombre = self.nombre_var.get()
        id_usuario = self.id_var.get()
        if nombre and id_usuario:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios.append(usuario)
            self.lista_usuarios.insert(tk.END, f"{nombre} (ID: {id_usuario})")
            self.nombre_var.set("")
            self.id_var.set("")
            self.lbl_result_usuarios.config(text="✅ Usuario registrado correctamente.")
        else:
            self.lbl_result_usuarios.config(text="⚠️ Complete todos los campos.")

    # --- Préstamos ---
    def interfaz_prestamos(self):
        ttk.Label(self.tab_prestamos, text="Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combo_usuarios = ttk.Combobox(self.tab_prestamos, state="readonly")
        self.combo_usuarios.grid(row=0, column=1)

        ttk.Label(self.tab_prestamos, text="Libro:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.combo_libros = ttk.Combobox(self.tab_prestamos, state="readonly")
        self.combo_libros.grid(row=1, column=1)

        ttk.Label(self.tab_prestamos, text="Fecha (AAAA-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        ttk.Entry(self.tab_prestamos, textvariable=self.fecha_var).grid(row=2, column=1)

        ttk.Button(self.tab_prestamos, text="Actualizar listas", command=self.actualizar_listas).grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Button(self.tab_prestamos, text="Prestar libro", command=self.prestar_libro).grid(row=4, column=0, columnspan=2, pady=5)
        ttk.Button(self.tab_prestamos, text="Ver préstamos", command=self.ver_prestamos).grid(row=5, column=0, columnspan=2, pady=5)

        self.lbl_resultado = tk.Label(self.tab_prestamos, text="", bg="#EBF5FB", fg="#1B2631", width=60, height=8, anchor="nw", justify="left", relief="groove")
        self.lbl_resultado.grid(row=6, column=0, columnspan=2, pady=10)

    def actualizar_listas(self):
        self.combo_usuarios["values"] = [u.nombre for u in self.usuarios]
        self.combo_libros["values"] = [l.titulo for l in self.libros]
        self.lbl_resultado.config(text="🔄 Listas actualizadas correctamente.")

    def prestar_libro(self):
        nombre = self.combo_usuarios.get()
        titulo = self.combo_libros.get()
        fecha = self.fecha_var.get()

        if not (nombre and titulo and fecha):
            self.lbl_resultado.config(text="⚠️ Complete todos los campos.")
            return

        usuario = next((u for u in self.usuarios if u.nombre == nombre), None)
        libro = next((l for l in self.libros if l.titulo == titulo), None)

        if usuario and libro:
            resultado = usuario.realizar_prestamo(libro, fecha)
            self.lbl_resultado.config(text=resultado)
        else:
            self.lbl_resultado.config(text="❌ Usuario o libro no encontrado.")

    def ver_prestamos(self):
        nombre = self.combo_usuarios.get()
        usuario = next((u for u in self.usuarios if u.nombre == nombre), None)
        if usuario:
            info = usuario.mostrar_prestamos()
            self.lbl_resultado.config(text=info)
        else:
            self.lbl_resultado.config(text="⚠️ Seleccione un usuario.")


# -------------------------
# EJECUCIÓN
# -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

