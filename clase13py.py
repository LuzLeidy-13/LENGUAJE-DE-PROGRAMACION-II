class Paciente:
    def __init__(self,nombre,dni):
        self.nombre = nombre
        self.dni = dni

class Cita:
    def __init__(self,paciente,fecha,especialidad):
        self.paciente = paciente
        self.fecha = fecha
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"paciente: {self.paciente.nombre}, DNI: {self.paciente,dni}, Fecha: {self.fecha}, Especialidad: {self.especialidad}")

class Consultorio:
    def __init__(self):
        self.citas = []
    def agendar_cita(self,nombre,dni,fecha,especialidad):
        paciente = Paciente(nombre,dni)
        cita= Cita(paciente,fecha,especialidad)
        self-citas.append(citas)
        print("citas agendadas corectamente")
    def mostrar_citas(self):
        if not self.citas:
            print("no hay citas agemdar")
        else:
            print("\nLista de citas agendadas")
            for cita in self,citas:
                cita.mostrar_informacion()

    def cancelar_cita(self,dni,fecha):
        for cita in self.cita:
            if cita.paciente.dni==cita.fecha==fecha:
                self.citas.remove(cita)
                print(f"cita del paciente{cita.paciente.nombre} cancelado")
                return
            print("cita no encontrada")

consultorio = Concultorio()

while True:
    print(" menu")
    print("1. agendar cita")
    print("2. mostrar todas las citas")
    print("3. cancelar citas")
    print("4. salir")

    opcion = input("selecione una opcion")
    if opcion = "1":
        nombre = input("nombre del paciente")
        dni = input("dni del paciente")
        fecha = input("fecha de la cita {DD/MM/AAAA}")
        especialidad = input("especialidad medica")
        conultorio.agendar_cita(nombre,dni,fecha,especialidad)
    elif opcion
