from read_csv import choose_data

def main():
    print('*****Bienvenido al graficador de Poblacion*****')
    choose = int(input('Ingrese 1 para graficar el modelo poblacional de un pais o ingrese otra tecla y enter para salir = '))
    
    if choose == 1:
        choose_data()
    else:
        return
         
if __name__ == '__main__':
    main()