def check_digit(run):
    mult = 2
    suma = 0
    for i in range(len(run)-1,-1,-1):
        suma += int(run[i]) * mult
        mult += 1
        if mult == 8 : mult = 2 
    
    digit = 11 - (suma % 11)
    if digit == 11 : digit = 0 
    if digit == 10 : digit = 'k'
    
    return digit

def RUN():
    while True:
        try:
            run=input('Ingrese el RUN(Sin puntos, con guion y digito verificador): ') 

            if not (len(run) == 10 and run[:8].isnumeric() and run[8]=='-'): raise Exception
            assert run[9] == str(check_digit(run[:8]))
            
            break
        
        except AssertionError:
            print('Error en la validacion del digito verificiador')
        except BaseException:
            print('Error en formato, intente: (12345678-9)')

    return run

def valid_name(text):
    while True:
        try:
            name = input(text)
            assert name.isalpha()
            break
        except AssertionError:
            print('La entrada no puede ser vacia, contener espacios y debe ser solo letras')
    return name

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





