#----- modulo para leer el acrhivo csv --------
import csv
import result_csv as result

def choose_data(validator):
  data = read_csv('C:/Users/maxte/Escritorio/Python_Projects/world_population/world_population.csv')
  if validator == 1:
    return continente_data(data)
  elif validator == 2:
    return world_pop_comparison(data)
  else:
    return world_pop_percentage(data)
  
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

def world_pop_comparison(data):
  world_pop_1970 = 0
  world_pop_1980 = 0
  world_pop_1990 = 0
  world_pop_2000 = 0
  world_pop_2010 = 0
  world_pop_2015 = 0
  world_pop_2020 = 0
  world_pop_2020 = 0
  world_pop_2022 = 0
  
  for country in data:
    
    world_pop_1970 += int(country["1970 Population"])
    world_pop_1980 += int(country["1980 Population"])
    world_pop_1990 += int(country["1990 Population"])
    world_pop_2000 += int(country["2000 Population"])
    world_pop_2010 += int(country["2010 Population"])
    world_pop_2015 += int(country["2015 Population"])
    world_pop_2020 += int(country["2020 Population"])
    world_pop_2022 += int(country["2022 Population"])
  
  world_pop_list = [world_pop_1970, world_pop_1980, world_pop_1990, world_pop_2000, world_pop_2010, world_pop_2015, world_pop_2020, world_pop_2022]
  result.graphic_population(world_pop_list)   

def world_pop_percentage(data):
  percentages_dict = {country["Country/Territory"]: country["World Population Percentage"] for country in data}
  names = percentages_dict.keys()
  per = percentages_dict.values()
  return result.generate_pie_chart('world_percentage',names, per)

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