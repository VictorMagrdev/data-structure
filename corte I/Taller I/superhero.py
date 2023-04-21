from colorama import ansi

class Superhero:
    def __init__(self):
        self.heroes_marvel= []
        self.all_heroes = []
        self.heroes_dc = []
        self.universo = ["Marvel", "DC"]
        self.nombre = ""
        self.superpoderes =[]
        self.creador = []        
    
    def add_hero(self):
            editorial = 0
            nombre = ""
            superpoderes =[]
            creador = []
            desicion = input(ansi.Fore.RESET +ansi.Fore.GREEN + 'Desida el univero: \n M marvel o D dc\n'+ ansi.Fore.RESET)
            if(desicion.capitalize() == 'M'):
                editorial = 0
            elif (desicion.capitalize() =='D'):
                editorial = 1
            nombre =input("ingrese el nombre de sus superheroe:\n")
            cant_poderes = int(input("cuantos poderes tiene su superheroe: \n"))
            
            for i in range(cant_poderes):
                superpoderes.append(input("Ingrese el superpoder: \n"))
            
            cant_autores = int(input("cuantos autores tiene el superheroe: \n"))
            for i in range(cant_autores):
                creador.append(input("Ingrese el creador: \n"))
            
            self.all_heroes.append((self.universo[editorial], nombre.capitalize() , superpoderes , creador))
            
            
    def seach_hero(self):
        name = input("ingrese el nombre del superheroe que desea buscar:\n")
        rango = len(self.all_heroes)
        for i in range(rango):
            if name.capitalize() == self.all_heroes[i][1]:
                poderes = self.all_heroes[i][2]
                print("Nombre: ") 
                print(name)  
                print(" poderes: ") 
                print(poderes)
            else:
                desicion = input("el heroe no esta registrado, ¿desea agregarlo? \n si o no")
                if desicion == "si":
                    self.add_hero()
                    
    def delete_hero(self):
        name = input("ingrese el nombre del superheroe que desea eliminar:\n")
        rango = len(self.all_heroes)
        for i in range(rango):
            if name.capitalize() == self.all_heroes[i][1]:
                self.all_heroes.pop(i)
        print("==============================")
        print(self.all_heroes)
        print("==============================")
    
    def powerfull_hero(self):
        mayor = 0
        posicion = 0
        for i in range(len(self.all_heroes)):
            cont = len(self.all_heroes[i][2])
            if cont > mayor:
                mayor = len(self.all_heroes[i][2])
                posicion = i
        print("=============powerfull=================")
        print(self.all_heroes[posicion])
        print("==============================")
        
    def less_hero(self):
        menor = 1000
        posicion = 0
        for i in range(len(self.all_heroes)):
            cont = len(self.all_heroes[i][2])
            if cont < menor:
                menor = len(self.all_heroes[i][2])
                posicion = i
        print("==============less powerfull================")
        print(self.all_heroes[posicion])
        print("==============================")
        
        
    def menu(self):
        response = 0
        inspiration = True
        while(inspiration):
            print(ansi.Fore.RESET +ansi.Fore.LIGHTRED_EX +"""
                1. crear superheroe
                2. buscar superheroe
                3. eliminar superheroe
                4. superheroe con mas poderes
                5. superheroe con menos poderes
                6. salir
                """ + ansi.Fore.RESET )
            response = int(input())
            if(response == 1):
                self.add_hero()
            elif(response == 2):
                self.seach_hero()
            elif(response == 3):
                self.delete_hero()
            elif(response == 4):
                self.powerfull_hero()
            elif(response == 5):
                self.less_hero()
            elif(response == 6):
                inspiration = False
            else:
                print("no se reconoce la instruccion digitada, intentelo de nuevo")