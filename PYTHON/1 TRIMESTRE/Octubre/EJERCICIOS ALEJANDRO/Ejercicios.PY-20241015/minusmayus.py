''' Programa que lea de teclado una letra minúscula y escriba la letra mayúscula correspondiente a la letra minúscula leída previamente '''
try: 
    # Leer una letra desde el teclado
    letra_minuscula = input("Introduce una letra minúscula: ")

    #Comprobamos que se haya introducido una única letra
    if len(letra_minuscula) != 1:
        raise ValueError("La entrada debe ser una única letra")
    
    # Comprobamos si es un carácter alfabético
    if not letra_minuscula.isalpha():
        raise ValueError("La entrada debe ser una letra")
    
    # Comprobar que la letra de entrada sea minúscula
    if not letra_minuscula.islower():
        raise ValueError("La letra debe ser minúscula")
    
    letra_mayuscula = letra_minuscula.upper()

    print(f"La letra mayus correspondiente es: {letra_mayuscula}")
except ValueError as e:
    print(f"Error: {e}")