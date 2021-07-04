
def enter_number(datatype,text='Ingrese numero'):
    number=""
    while(type(number)!=datatype or number<=0):
        try:
            number=datatype(input(text))
        except:
            print('Debe ser un numero')
    return number

def in_range_number(min,max,text):    
    data=enter_number(int,text)
    while data<min or data>max:
        data=enter_number(int,text)
    return data





