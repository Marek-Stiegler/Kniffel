from random import *


class Dices:
    
    def __init__(self):
        self.__list_values = [0, 0, 0, 0, 0]
        self.__list_locked = [False, False, False, False, False]
        
    
    
    def shake(self) -> None:
        for i in range(len(self.__list_values)):
            if self.__list_locked[i] == False:
                self.__list_values[i] = randint(1, 7)
    

    def get_list_values(self) -> list:
        return self.__list_values
        
    
    def set_lock(self) -> None:
        #Entscheidung, welche Würfel festgehalten werden sollen
        lock = input("Welche Würfel möchten Sie festhalten?")    
        lock.split(",")
        x = len(lock)

        #Übertragung in list_locked
        while x < 0:
            self.__list_locked[lock[x-1]] = True
            lock.pop()
            x = len(lock)
  

    def __str__(self):
        text = str(self.__list_values + self.__list_locked)
        return text
    
    
dice = Dices()
dice.shake
dice.set_lock