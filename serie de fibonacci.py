def fibonacci(n):
    a, b = 0, 1
    print(a, end=" ")
    
    if n > 1:
        print(b, end=" ")
    
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

def main():
    try:
        n = int(input("ingrese numero de series "))
        
        if n <= 0:
            raise ValueError("Debe ingresar un número entero positivo.")
        
        fibonacci(n)
    
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    main()
