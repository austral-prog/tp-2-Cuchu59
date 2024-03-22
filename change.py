def change():
    expense = 23.75
    money = 100
    diff = money - expense
    
    pesos = int(diff)
    centavos = diff - pesos
    
    print('')
    print('VUELTO')
    print('')
    print('PESOS:')
    print(pesos) 
    print('CENTAVOS:')
    print(int(centavos * 100))
