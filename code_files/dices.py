from random import *


class Dices:
    
    def __init__(self):
        self.__list_values = [0, 0, 0, 0, 0]
        self.__list_locked = [False, False, False, False, False]
        
    
    
    def shake(self) -> None:
        for i in range(len(self.__list_values)):
            if self.__list_locked[i] == False:
                self.__list_values[i] = randint(1, 6)
    

    def get_list_values(self) -> list:
        return self.__list_values
    

    def get_list_locked(self) -> list:
        return self.__list_locked
        
    
    def set_lock(self) -> None:
        #Entscheidung, welche Würfel festgehalten werden sollen
        lock = input("Welche Würfel möchten Sie festhalten?")    
        lock = lock.split(",")

        #Übertragung in list_locked
        for i in lock:
            self.__list_locked[int(i)] = True #todo: -1 für gute darstellung



    def __str__(self):
        text = ''
        for i in range(5):
            if self.__list_locked[i] == False:
                text += str(self.__list_values[i])
                text += ' '

            else:
                text += f'<{self.__list_values[i]}>'
                text += ' '

        return text



#main 

dice = Dices()
dice.shake()
print(dice)
dice.set_lock()
print(dice)