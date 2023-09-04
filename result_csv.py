import matplotlib.pyplot as plt 
#plt es un alias para matplotlib.pyplot

def graphic_country(continent):
  while True: 
    abv = str(input('Ingrese la abreviacion del pais a graficar = ')).upper()
    country = next((country for country in continent if abv == country['CCA3']), None)
    if country:
      labels = [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]
      values = [
        int(country["1970 Population"]), 
        int(country["1980 Population"]), 
        int(country["1990 Population"]), 
        int(country["2000 Population"]), 
        int(country["2010 Population"]), 
        int(country["2015 Population"]), 
        int(country["2020 Population"]), 
        int(country["2022 Population"])
      ]
      generate_bar_chart(labels, values)
      break
    else:
      print("Abreviación incorrecta. Intente de nuevo.")

# funcion para grafico de barra
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
  ax.bar(labels, values)
  #aquí se indica que se generará una gráfica de barras (bar), y se envia labels y values para que sepa que tiene que crear el gráfico con esos valores
  plt.xlabel('Año')
  # Eje x
  plt.ylabel('Población')
  #Eje Y
  plt.title('Población a lo largo de los años')
  #Titulo del grafico
  plt.show()
  #muestra la grafica de barras