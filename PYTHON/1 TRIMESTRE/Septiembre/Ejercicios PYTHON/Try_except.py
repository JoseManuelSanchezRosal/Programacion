#Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario no introduce números 
# debe devolver un aviso de error y si el divisor es cero también.
try:
    dividendo = float(input("Introduce dividendo: "))
    print(dividendo)
 
except ValueError:
    print("Error, introduzca número: ")

try:
    divisor = float(input("introduce divisor: "))

except ValueError:
        print("Error, introduzca número: ")

if divisor == 0:
     print("Error, el dividendo no puede ser 0")
else:
     print(dividendo / divisor)

# Esta función permite ejecutar el programa TRY, excepto si el valor es erróneo, que entonces se ejecutaría lo que hay en "EXCEPT". 
# En EXCEPT configuramos la estructura del error. Se pueden confugurar varios "EXCEPT (ejem ZERODIVISIONERROR)