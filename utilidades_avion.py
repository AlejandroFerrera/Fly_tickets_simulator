import validadores as val
import numpy as np
import locale
locale.setlocale(locale.LC_ALL,'')

x_roja = '\033[91m'+'\033[1m'+'X '+'\033[0m'
                                                                    #IMPRIMIR 
def print_line(rango_filas,array,space = False):
    
    cant_columnas = len(array[0])

    for fila in range(rango_filas[0],rango_filas[1]):
        for columna in range(cant_columnas):
            if columna == 0: print('|',end=" ")
            if columna == 2:
                print(array[fila,columna],end="\t     ") 
            else:
                if (len(str(array[fila,columna]))==1): 
                    print(array[fila,columna],end="    ")
                else:
                    print(array[fila,columna],end="   ")
        else : print('|')
        if space == True : print()
        if fila != rango_filas[1]-1 : print()


def print_fly(array):
    print('\t      ASIENTOS:\n')
    print_line((0,5),array)
    print("""+-------------       ---------------+
|                                   |
+-------------       ---------------+""")
    print_line((5,7),array,space = True)


def print_sales(sales_record):
    print('\nNro.Asiento:\t\tCliente:')
    for element in sales_record:
        print(f'    {element[0]}    \t\t{element[2].get("run")},{element[2].get("Name")}')
                                                    
                                                                  #REGISTRO DE CLIENTES

def register_client():
    
    run = val.RUN()

    name = val.valid_name('Ingrese nombre: ')
    
    phone = val.in_range_number(10000000,99999999,'Ingrese telefono(8 Digitos) +569:')
    
    bank = val.in_range_number(1,2,'Su Banco es BANCO-DUOC?: 1-SI 2-NO: ')
    
    bank = 'bancoDuoc' if bank == 1 else 'otro'

    return {'run': run, 'Name': name.capitalize(), 'Phone': phone,'Bank':bank}
                                                                   
                                                                   #GESTOR DE TICKETS
def buy_ticket(number,array,sales_record):
    total = 0
    pos = np.where (array == number)

 #El metodo where devuelve una tupla con 2 arrays donde pos[0] es un array que contiene la fila donde se encuentra el elemento buscado
 #si este array esta vacio significa que no encontro el numero de asiento(tambien podria usarse con len(pos[1]) <--columna ,siguiendo esta logica :D

    while len(pos[0]) == 0:                  
        number = val.in_range_number(1,42,'El asiento no se encuentra disponible, intente con otro: ')
        pos = np.where (array == number)

    array[pos] = x_roja                          
    cliente = register_client()
    sales_record.append((number,pos,cliente)) 
    
#Los registros de venta son una tupla de 3 elementos, donde el primer elemento es el numero de asiento,
#segundo la posicion dentro del array para facilitar la anulacion posteriormente y por ultimo los datos del cliente.

    if number < 31:
        total = 78900
    else:
        total = 240000
    if cliente['Bank'] == 'bancoDuoc' : total *= 0.85
    
    print(f'\nHa comprado el asiento {number}, su total a pagar es {locale.currency(total,grouping=True)}')
    

def delete_ticket(number,array,sales_record):
    for element in sales_record:
        if element[0] == number:
            array[element[1]] = number       
            sales_record.remove(element)
            print(f'\nSe ha anulado la compra del asiento {number} perteneciente a {(element[2].get("Name"))}')
            break
    else:
        print('\nEl asiento no ha sido vendido')

def modify(number,sales_record):
    
    for element in sales_record:
        if element[0] == number:
            run_to_check = val.RUN()
            if run_to_check == element[2].get('run'):
                
                option = val.in_range_number(1,2,'Que dato desea modificar:\n1-Nombre\n2-Telefono\n-->')

                if option == 1:
                    name = val.valid_name('Ingrese nombre para actualizar: ')
                    element[2]['Name'] = name
                    print('\nNombre actualizado')
                
                if option == 2:
                    phone = val.in_range_number(10000000,99999999,'Ingrese nuevo telefono(8 Digitos) +569: ')
                    element[2]['Phone'] = phone
                    print(f'\nTelefono de {element[2].get("Name")} modificado')
            else:
                print('\nEl numero de asiento no coincide con el RUN')
            break
    else:
        print('\nEl asiento no ha sido vendido')
            

