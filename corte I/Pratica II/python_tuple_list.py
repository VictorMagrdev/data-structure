class TupleList:
    def __init__(self):
        self.countries_list = []
        self.country_name = " "
        self.population = 0
        self.continent = ""
        
def total_countries(self):
    print('         ingresa la siguiente informacion')
    print("========================================================")
    while True:
        try:
            number_countries = int(input('cantidad a añadir: '))
            for country in range(number_countries):
                self.country_name = input('     País >> ')
                self.population = int(input('    Poblacion >> '))
                self.continent = input('    Continete >> ')
                print('-------------------------------------------')
            self.countries_list.append(self.country_name, self.population, self.continent)
        except ValueError:
            print('error de tipo de dato suministrado')