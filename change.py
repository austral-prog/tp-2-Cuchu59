def change():
    expense = 23.75
    money = 100
    diff = money - expense
    
    pesos = int(diff)
    centavos = (diff - pesos)*100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print('')
    print('Vuelto')
    print('')
    print('Pesos:')
    print(pesos) 
    print('Centavos:')
    print(int(centavos))
