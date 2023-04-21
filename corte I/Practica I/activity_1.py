'''
    Data type: list pactice
    Date: 25/01/23
'''

# 1. Declarar la clase
class ListPractice:
    # 2. Crear función inicializadora de la clase
    def __init__(self):
        # 3. Definir las variables globales de la clase
        self.student_name = "juan"
        self.courses_list = ['POO', 'TAD']
    
    # 4. Funcion customizada
    def show_info_list(self):
        # imprimir el contenido de courses_list
        print(self.courses_list)
        # Cantidad de elementos que tiene la lista
        print(len(self.courses_list))
        
    #5. Funcion que solicita al usuario ingresar información
    def input_data_courses(self):
        
        #1. declaramos una variable a nivel de metodo
        print('Ingrese la siguiente informacion: ')
        
        #Solicitud de texto
        self.student_name = input("Nombre: ")
        
        #Solicitud de numero entero
        courses_number = int(input("Cantidad de asignaturas: "))
        
        #validamos si el courses_number es menor que el tamaño de la lista
        if courses_number <= len(self.courses_list):
            print(' >> Error: Cursos a inscribir es menor que 2 <<')
        else:
            if(len(self.courses_list) != 0 and len(self.courses_list) > 0):
                courses_number = courses_number - len(self.courses_list)
                
            #solicitar nombre de las asignaturas al usuario
            for course in range(courses_number):
                #Variable que almacena el nombre de la asignatura
                courses_name = input('Nombre asignatura: ')
                if(courses_name in self.courses_list):
                    print("ya existe esta materia")
                    continue
                else:
                    self.courses_list.append(courses_name)
            print(self.courses_list)
