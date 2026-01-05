class ConversorTemperatura:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    @classmethod
    def desde_celsius(cls, c):
        f = cls.celsius_a_fahrenheit(c)
        return cls(f)

    @staticmethod
    def celsius_a_fahrenheit(c):
        return (c * 9/5) + 32

t1 = ConversorTemperatura(77)
print(t1.fahrenheit)

t2 = ConversorTemperatura.desde_celsius(0)
print(t2.fahrenheit)

print(ConversorTemperatura.celsius_a_fahrenheit(100))
