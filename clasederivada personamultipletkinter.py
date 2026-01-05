import tkinter as tk

# ---------------------------
# CLASES LÓGICAS
# ---------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        return f"Trabajo como {self.profesion} y gano {self.salario} al mes."

class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        return f"Estudio {self.carrera} en la universidad {self.universidad}."

class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_informacion(self):
        return (
            f"===== INFORMACIÓN DE {self.nombre.upper()} =====\n\n"
            f"{self.presentarse()}\n"
            f"{self.trabajar()}\n"
            f"{self.estudiar()}\n"
        )

# ---------------------------
# INTERFAZ GRÁFICA
# ---------------------------
personas = []

def agregar_persona():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    profesion = entry_profesion.get()
    salario = entry_salario.get()
    carrera = entry_carrera.get()
    universidad = entry_universidad.get()

    if not nombre or not edad or not profesion or not salario or not carrera or not universidad:
        texto_salida.delete("1.0", tk.END)
        texto_salida.insert(tk.END, "⚠️ Complete todos los campos antes de agregar.")
        return

    try:
        edad = int(edad)
        salario = float(salario)
    except ValueError:
        texto_salida.delete("1.0", tk.END)
        texto_salida.insert(tk.END, "❌ Edad debe ser número entero y salario un número válido.")
        return

    persona = PersonaMultirol(nombre, edad, profesion, salario, carrera, universidad)
    personas.append(persona)

    listbox_personas.insert(tk.END, persona.nombre)
    texto_salida.delete("1.0", tk.END)
    texto_salida.insert(tk.END, f"✅ Persona '{nombre}' agregada correctamente.\n")
    limpiar_campos()

def mostrar_persona_seleccionada(event=None):
    seleccion = listbox_personas.curselection()
    texto_salida.delete("1.0", tk.END)

    if not seleccion:
        texto_salida.insert(tk.END, "⚠️ Selecciona una persona de la lista para ver su información.")
        return

    indice = seleccion[0]
    persona = personas[indice]
    texto_salida.insert(tk.END, persona.mostrar_informacion())

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_profesion.delete(0, tk.END)
    entry_salario.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    entry_universidad.delete(0, tk.END)

# ---------------------------
# VENTANA PRINCIPAL
# ---------------------------
root = tk.Tk()
root.title("Personas Múltiples - Información en el mismo cuadro")
root.geometry("550x630")
root.config(bg="#e8f4f4")

# Título
tk.Label(root, text="Registro de Personas Múltiples", font=("Arial", 13, "bold"), bg="#e8f4f4").pack(pady=5)

# Entradas de datos
def crear_campo(texto):
    tk.Label(root, text=texto, bg="#e8f4f4").pack()
    entrada = tk.Entry(root, width=45)
    entrada.pack()
    return entrada

entry_nombre = crear_campo("Nombre:")
entry_edad = crear_campo("Edad:")
entry_profesion = crear_campo("Profesión:")
entry_salario = crear_campo("Salario:")
entry_carrera = crear_campo("Carrera:")
entry_universidad = crear_campo("Universidad:")

# Botón para agregar
tk.Button(root, text="Agregar persona", command=agregar_persona, bg="#4CAF50", fg="white", width=25).pack(pady=8)

# Lista de personas
tk.Label(root, text="Seleccione una persona:", font=("Arial", 10, "bold"), bg="#e8f4f4").pack()
listbox_personas = tk.Listbox(root, width=45, height=5, selectmode=tk.SINGLE)
listbox_personas.pack(pady=5)

# Vincular evento de selección
listbox_personas.bind("<<ListboxSelect>>", mostrar_persona_seleccionada)

# Cuadro de texto para mostrar resultados (en el mismo cuadrante)
texto_salida = tk.Text(root, height=12, width=60, bg="#f9f9f9", fg="#333")
texto_salida.pack(pady=10)

# Ejecutar aplicación
root.mainloop()
