def in_range_number(min,max,text,dtype = int):    
    number = min - 1
    while number < min or number > max:
        try:
            number = dtype(input(text))
            assert number >= min and number <= max
        except ValueError:
            print('Debe ser un valor entero')
        except AssertionError:
            print('El numero no se encuentra dentro del rango indicado')        
    
    return number





