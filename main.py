from read_csv import choose_data

def main():
    print('*****Bienvenido al graficador de Poblacion*****')
    print('Ingrese 1 para graficar el modelo poblacional de un pais. \nIngrese 2 para graficar poblacion mundial. \nIngrese 3 para graficar porcentaje de poblacion mundial. \nO ingrese otra tecla y enter para salir.')
    choose = int(input('=> '))
    
    if choose == 1:
        choose_data(choose)
    elif choose == 2:
        choose_data(choose)
    elif choose == 3:
        choose_data(choose)
    else:
        return
         
if __name__ == '__main__':
    main()