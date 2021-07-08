def dig_verificador(run):
    mult = 2
    suma = 0
    for i in range(len(run)-1,-1,-1):
        suma += int(run[i]) * mult
        mult += 1
        if mult == 8 : mult = 2 
    
    digito = 11 - (suma % 11)
    if digito == 11 : digito = 0 
    if digito == 10 : digito = 'k'
    
    return digito

def RUN():
    while True:
        try:
            run=input('Ingrese el RUN(Con guion y digito verificador): ') 

            if not (len(run) == 10 and run[:8].isnumeric() and run[8]=='-'): raise Exception
            assert run[9] == str(dig_verificador(run[:8]))
            
            break
        
        except AssertionError:
            print('Error en la validacion del digito verificiador')
        except BaseException:
            print('Error en formato, intente: (12345678-9)')

    return run

def nombre_valido():
    while True:
        try:
            nombre = input('Ingrese nombre: ')
            assert nombre.isalpha()
            break
        except AssertionError:
            print('El nombre no puede ser vacio, contener espacios y deben ser solo letras')
    return nombre

def in_range_number(min,max,text,dtype = int):    
    while True:
        try:
            number = dtype(input(text))
            assert number >= min and number <= max
            break
        except ValueError:
            print('Debe ser un valor entero')
        except AssertionError:
            print('El numero no se encuentra dentro del rango indicado')        
    
    return number





