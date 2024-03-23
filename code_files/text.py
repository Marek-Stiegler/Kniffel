#Entscheidung, welche Würfel festgehalten werden sollen

lock = input("Welche Würfel möchten Sie festhalten?")    
lock = lock.split(",")
x = len(lock)

print(lock)
#Übertragung in list_locked
# while x < 0:
#     self.__list_locked[lock[x-1]] = True
#     lock.pop()
#     x = len(lock)