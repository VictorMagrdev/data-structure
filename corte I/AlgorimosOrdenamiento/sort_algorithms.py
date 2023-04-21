from random import sample
from colorama import Fore, init

class SortAlgoritms:
    def __init__(self):
        self.number_list = range(100)
        self.list_burble_sort = sample(self.number_list,8)
        self.list_select_sort = sample(self.number_list,8)
        self.list_insert_sort = sample(self.number_list,8)
        self.list_merge_sort = sample(self.number_list,8)
        self.list_quick_sort = sample(self.number_list,8)
        self.list_radix_sort = sample(self.number_list,8)
        
    def burble_sort_function(self):
        print("============================================================")
        count_item_list = 0
        for i in self.list_burble_sort:
            count_item_list +=1
        print(count_item_list)
        
        for j in range(count_item_list-1):
            print(j)
            for k in range(count_item_list-j-1):
                if self.list_burble_sort[k] > self.list_burble_sort[k+1]:
                    self.list_burble_sort[k], self.list_burble_sort[k+1] = self.list_burble_sort[k+1], self.list_burble_sort[k]
        print(self.list_burble_sort)
        
    def merge_sort(self,lista):
        if len(lista) < 2:
            return lista
        else:
                middle = len(lista) // 2
                right = self.merge_sort(lista[:middle])
                left = self.merge_sort(lista[middle:])
                return self.merge(right, left)
        
    def merge(lista1, lista2):
        i, j = 0, 0 
        result = []
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i] < lista2[j]):
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1
        result += lista1[i:]
        result += lista2[j:]
        return result
