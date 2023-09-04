#----- modulo para leer el acrhivo csv --------
import csv
import result_csv as result

def choose_data():
  data = read_csv('C:/Users/maxte/Escritorio/Python_Projects/world_population/world_population.csv')
  return continente_data(data)
  
def continente_data(data):
  continent = int(input('Ingrese 1- Sudamerica. 2- Norteamerica. 3- Africa. 4- Oceania. 5- Europa. 6- Asia = '))
  if continent == 1:
    continent_filter = 'South America'
    return filter_country(continent_filter, data)
  elif continent == 2:
    continent_filter = 'North America'
    return filter_country(continent_filter, data)
  elif continent == 3:
    continent_filter = 'Africa'
    return filter_country(continent_filter, data)
  elif continent == 4:
    continent_filter = 'Oceania'
    return filter_country(continent_filter, data)
  elif continent == 5:
    continent_filter = 'Europe'
    return filter_country(continent_filter, data)
  elif continent == 6:
    continent_filter = 'Asia'
    return filter_country(continent_filter, data)
   
def filter_country(continent, data):
  continent_filter = lambda pais: pais['Continent'] == continent
  region = list(filter(continent_filter, data))
  for pais in region:
    print(f"Paises que ocupan el continente {continent} -> Abreviacion: {pais['CCA3']}. -> {pais['Country/Territory']}")
  return result.graphic_country(region)
    
# funcion abrir archivo
def read_csv(path):
  with open(path, 'r') as csvfile:
    # funcion que se encarga de leer el csv y delimitar las celdas por comas
    reader = csv.reader(csvfile, delimiter = ',')
    # nombre de las columnas se encuentra en la primera fila
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row) # une los valores de la listas en tuplas
      country_dict = {key : value for key, value in iterable}
      data.append(country_dict)
    return data

