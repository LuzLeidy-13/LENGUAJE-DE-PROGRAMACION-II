class gestordetareas:
    def __init__(self):
        self.tareas = {}

    def agregartarea(self,tarea):
        self.tareas.aappend(tarea)
        print ("tarea agregada")

    def mostrartareas(self):
        if not self.tareas:
            print("no hay tareas pendientes")
        else:
            print("tareas pendientes")
            for i,tarea in enumerate (self,tareas,1):
                print (f"{i} {tarea}")

mi_gestor = gestordetareas()

while True:
    print("---menu---")
    print("1.agregar tarea")
    print("2.mostrar tarea")
    print("3.salir")
    opcion = input ("seleccione una opcion")

    if opcion == "1":
        tarea = input("escribe la tarea: ")
        mi_gestormostrar_tarea(tarea)
    elif opcion == "2":
        mi_gestormostrar_tareas()
    elif opcion == "3":
        print("saliendo del grator de tarea :")
        break
    else:
        print("opncion no valida. intente de nuevo ")
