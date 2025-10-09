class ConvertidorTemperatura:
    def __init__(self):
        """
        Inicializa la clase ConvertidorTemperatura.
        Atributos privados para almacenar las temperaturas.
        """
        self._celsius = None
        self._fahrenheit = None

    @property
    def celsius(self):
        """Getter para la temperatura en Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """
        Setter para la temperatura en Celsius.
        Al establecer un valor en Celsius, actualiza automáticamente Fahrenheit.
        """
        self._celsius = valor
        self._fahrenheit = (valor * 9/5) + 32

    @property
    def fahrenheit(self):
        """Getter para la temperatura en Fahrenheit."""
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """
        Setter para la temperatura en Fahrenheit.
        Al establecer un valor en Fahrenheit, actualiza automáticamente Celsius.
        """
        self._fahrenheit = valor

        self._celsius = (valor - 32) * 5/9

convertidor = ConvertidorTemperatura()

# 1. Convertir de Fahrenheit a Celsius
temperatura_f = 68.0
print(f"Estableciendo temperatura en Fahrenheit: {temperatura_f}°F")
convertidor.fahrenheit = temperatura_f
print(f"Temperatura convertida a Celsius: {convertidor.celsius:.2f}°C")

print("-" * 20)

# 2. Convertir de Celsius a Fahrenheit
temperatura_c = 25.0
print(f"Estableciendo temperatura en Celsius: {temperatura_c}°C")
convertidor.celsius = temperatura_c
print(f"Temperatura convertida a Fahrenheit: {convertidor.fahrenheit:.2f}°F")
