import numpy as np
import utilidades_avion as ut
import locale
import validadores as val
locale.setlocale(locale.LC_ALL,'')

avion = np.arange(1,43,dtype='object').reshape(7,6)
ventas = []

opcion = 0
while opcion!=6:
    try:
        opcion=int(input('\nBIENVENIDO A VUELOS-DUOC:\n\n1-Ver asientos disponibles \n2-Comprar asiento \n3-Anular vuelo \n4-Modificar datos de pasajero\n5-Ver registro de ventas \n6-Salir \n--> '))
    except:
        print('Solo numeros por favor')  
    
    if opcion == 1:
        ut.print_fly(avion)
    
    elif opcion == 2:
        print(f'\nPrecio asiento normal(1-30): {locale.currency(78900,grouping=True)}')
        print(f'Precio asiento VIP(31-42):   {locale.currency(240000,grouping=True)}\n')
        
        asiento = val.in_range_number(1,42,'Que asiento desea comprar(Entre 1 y 42): ')   
        ut.buy_ticket(asiento,avion,ventas)
  
    elif opcion == 3:
        if len(ventas) == 0:
            print('\nAun no se han comprado vuelos')
        else:
            asiento = val.in_range_number(1,42,'Que asiento desea anular(Entre 1 y 42): ')   
            ut.delete_ticket(asiento,avion,ventas)
    
    elif opcion == 4:
        if len(ventas) == 0:
            print('\nAun no se han comprado vuelos')
        else:
            asiento = val.in_range_number(1,42,'De que asiento desea modificar datos del cliente(Entre 1 y 42): ')   
            ut.modify(asiento,ventas)

    elif opcion == 5:
        if len(ventas) == 0:
            print('\nAun no se han comprado vuelos')
        else:
            ut.print_sales(ventas)
    elif opcion == 6:
        print('\nGracias por preferir Vuelos-DUOC!!!')
    else:
        print('No existe esa opcion')


        


    
    




