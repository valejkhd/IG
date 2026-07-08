def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
def sumadigitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumadigitos(n // 10)
def fibonacci(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)
def suma_valores(n):
                if n == 1:
                    return 1
                else:
                    return n + suma_valores(n - 1)
def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Factorial")
        print("2. Potencia")
        print("3. Suma de dígitos")
        print("4. Fibonacci")
        print("5. Suma de valores")
        print("6. Salir")
        opcion = int(input("Ingrese el número de la opción deseada: "))
        
        if opcion == 1:
            n = int(input("Ingrese un número para calcular su factorial: "))
            print(f"El factorial de {n} es: {factorial(n)}")
        elif opcion == 2:
            base = float(input("Ingrese la base: "))
            exponente = int(input("Ingrese el exponente: "))
            print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")
        elif opcion == 3:
            n = int(input("Ingrese un número para calcular la suma de sus dígitos: "))
            print(f"La suma de los dígitos de {n} es: {sumadigitos(n)}")
        elif opcion == 4:
            n = int(input("Ingrese un número para calcular su Fibonacci: "))
            print(f"El término {n} de la serie Fibonacci es: {fibonacci(n)}")
        elif opcion == 5:
            n = int(input("Ingrese un número para calcular la suma de valores hasta ese número: "))
            print(f"La suma de los valores hasta {n} es: {suma_valores(n)}")
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
menu()