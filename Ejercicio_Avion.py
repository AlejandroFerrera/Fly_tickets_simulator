import numpy as np
from utilidades_avion import *
import locale
import validadores as val
locale.setlocale(locale.LC_ALL,'')

plane = np.arange(1,43,dtype='object').reshape(7,6)
sales = []

while True:
    option = val.in_range_number(1,6,'\nBIENVENIDO A VUELOS-DUOC:\n\n1-Ver asientos disponibles \n2-Comprar asiento \n3-Anular vuelo \n4-Modificar datos de pasajero\n5-Ver registro de sales \n6-Salir \n--> ')
    
    if option == 1:
        print_fly(plane)
    
    elif option == 2:
        print(f'\nPrecio asiento normal(1-30): {locale.currency(78900,grouping=True)}')
        print(f'Precio asiento VIP(31-42):   {locale.currency(240000,grouping =True)}\n')
        
        seat = val.in_range_number(1,42,'Que asiento desea comprar(Entre 1 y 42): ')   
        buy_ticket(seat,plane,sales)
  
    elif option == 3:
        if len(sales) == 0:
            print('\nAun no se han comprado vuelos')
        else:
            seat = val.in_range_number(1,42,'Que asiento desea anular(Entre 1 y 42): ')   
            delete_ticket(seat,plane,sales)
    
    elif option == 4:
        if len(sales) == 0:
            print('\nAun no se han comprado vuelos')
        else:
            seat = val.in_range_number(1,42,'De que asiento desea modificar datos del cliente(Entre 1 y 42): ')   
            modify_ticket(seat,sales)

    elif option == 5:
        if len(sales) == 0:
            print('\nAun no se han comprado vuelos')
        else:
            print_sales(sales)
    elif option == 6:
        print('\nGracias por preferir Vuelos-DUOC!!!')
        break



        


    
    




