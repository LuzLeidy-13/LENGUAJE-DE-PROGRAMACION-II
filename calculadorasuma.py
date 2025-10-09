
class calculadorasuma:
    def __init__(self):
        self.total = 0
        
    def sumarnumeros (self):
        print(" calcula la suma de numeros ingresados ")
        print("escribenumeros para sumar. escribe´fin´para terminar" )
        entrada=" "
        while entrada.lower() != "fin":
            entrada = input (" ingrese un numero : ")
            if entrada.isdigit():
                self.total+= int(entrada)
                if numero == 0:
                    print("el numero ingresado es nulo")
                elif numero %2 == 0:
                    print

    
                
            elif entrada.lower()!= "fin":
                print("entrada invalida: escriba un numero o ´fin´ ")
            print(f"la suma total es: {self.total}")
            

def main():
    calculadora = calculadorasuma()
    calculadora.sumarnumeros()
    
if __name__=="__main__":
    main()
