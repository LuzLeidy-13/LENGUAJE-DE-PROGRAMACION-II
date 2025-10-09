class Persona:
    def __init__(self, nombre, peso_kg, altura_m):
        """
        Inicializa la clase Persona con nombre, peso en kg y altura en m.
        
        Atributos:
        nombre (str): El nombre de la persona.
        peso_kg (float): El peso de la persona en kilogramos.
        altura_m (float): La altura de la persona en metros.
        """
        self.nombre = nombre
        self.peso_kg = peso_kg
        self.altura_m = altura_m

    def calcular_imc(self):
        """
        Calcula el Índice de Masa Corporal (IMC) de la persona.
        Fórmula: IMC = peso (kg) / [altura (m)]^2
        """
        if self.altura_m <= 0:
            return "Error: La altura debe ser mayor que cero."
        
        imc = self.peso_kg / (self.altura_m ** 2)
        return imc

    def clasificar_imc(self, imc):
        """
        Clasifica el IMC según la tabla de la OMS.
        """
        if isinstance(imc, str):
            return imc
            
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            return "Normal"
        elif 25.0 <= imc <= 29.9:
            return "Sobrepeso"
        elif 30.0 <= imc <= 34.9:
            return "Obesidad grado I"
        elif 35.0 <= imc <= 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III (mórbida)"


persona1 = Persona("roberto", 64.7, 1.64)

imc_juan = persona1.calcular_imc()
clasificacion_juan = persona1.clasificar_imc(imc_juan)

print(f"Nombre: {persona1.nombre}")
print(f"Peso: {persona1.peso_kg} kg")
print(f"Altura: {persona1.altura_m} m")
print(f"IMC: {imc_juan:.2f}")  
print(f"Clasificación: {clasificacion_juan}")

print("\n--- Otro ejemplo ---")
persona2 = Persona("compañero", 51, 1.56)
imc_ana = persona2.calcular_imc()
clasificacion_ana = persona2.clasificar_imc(imc_ana)

print(f"Nombre: {persona2.nombre}")
print(f"IMC: {imc_ana:.2f}")
print(f"Clasificación: {clasificacion_ana}")
