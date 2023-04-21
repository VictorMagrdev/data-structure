'''
    List methods
    Date: 27/01/23
'''

class ListMethods:
    
    def __init__(self):
        self.pets = []
        self.vehicles = list()
    
    def add_list_elements(self):
        self.pets.append("dog")
        self.pets.append("cat")
        print(self.pets)
    
    def input_data_vehicles_list(self):
        vehicles_number = int(input('Cuantos vehiculos tiene: '))
        for vehicle_item in range (vehicles_number):
            vehicle_type = input('Tipo de vehiculo: ')
            self.vehicles.append(vehicle_type)
        print(self.vehicles)
        
    def show_collection_data_list(self):
        print(self.vehicles[2:4])
        print(self.vehicles[:])
        print(self.vehicles[2:])
        print(self.vehicles[2])
        print(self.vehicles[::2])
        print(self.vehicles[1:5:2])
        
    def iteration_list(self):
        for item in self.vehicles:
            print(item)
            if "Carro".capitalize in self.vehicles:
                print("si se encontro el valor")
            else:
                print("no se encontro el valor")
    
    def add_elements(self):
        
        self.vehicles.extend(["Carro", "Tractomula", "Avion"])
        print(self.vehicles)
        
    def add_specific_element(self):
        self.vehicles.insert(0, 'Moto')
        print(self.vehicles)
        
    def remove_last_element(self):
        self.vehicles.pop()
        print(self.vehicles)
        
    def remove_specific_element(self):
        self.vehicles.pop(0)
        print(self.vehicles)
        
    def remove_element_by_name(self):
        x = input("introdusca el elemento que desea eliminar: ")
        self.vehicles.remove(x)
        print(self.vehicles)
        
    def remove_all_mach_elements(self):
        new_list = list(filter(('tractomula').__ne__,self.vehicles))
        print(new_list)