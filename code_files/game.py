from dices import Dices
from paper import Paper, Paper_top,Paper_bottom

class Game:
    def __init__(self):
        self.__finished = False
        self.__trycount = 0
        #!Ausgeben der Amleitung
        print("Anleitung")
        #Erschaffen + Ausgeben des Paper
        self.paper_top = Paper_top()
        self.paper_bottom = Paper_bottom()
        print("ones:\ntwos:\nthrees:\nfours:\nfives:\nsixes:\n\nthree of a kind:\nfour of a kind:\nfull house:\nsmall straight:\nlong straight:\nchance:\nkniffel:")
        #Erschaffen der Dice
        self.dices=Dices()

    def play(self):
        for _ in range(13):
            while self.__finished == False:
                self.__trycount += 1
                locked = self.dices.get_list_locked()
                if all(locked) == True:
                    self.__trycount = 0
                    self.__finished = True

                if self.__trycount > 3:
                    self.__trycount = 0
                    self.__finished = True    
                self.dices.shake()
                l = self.dices.get_list_values()
                print(f"{self.paper_top}\n{self.paper_bottom}")
                self.paper_top.set_list_values(l)
                self.paper_bottom.set_list_values(l)
                print(self.dices)
                print(f"{self.paper_top}\n{self.paper_bottom}")
                self.set_lock()
                e = str(input("Möchten sie diese Punkte eintragen? (J/N)  "))
                while e == "J":
                    v = str(input(("Wo eintragen? (Angabe als Ones/Twos/Threes/...)")))
                    first = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
                    second = ['Three of a Kind', 'Four of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Chance', 'Kniffel']
                    if v in first:
                        valid = self.paper_top.add_fixed_value(int(self.paper_top.index(v)))
                        if valid == True:
                            e = "N"
                    elif v in second:
                        valid = self.paper_bottom.add_fixed_value(int(self.paper_bottom.index(v)))
                        if valid == True:
                            e = "N"
                    print("Etwas wurde falsch geschrieben. :( \n\n Bitte halten sie sich an die Spielregeln")
        
        
        bonus = 0
        summe_top = self.paper_top.get_points()
        summe_bottom = self.paper_bottom.get_points()
        print(self.paper_top)
        print(f"Summe Oben:{summe_top}")
        if summe_top >= 63:
            bonus = 35
        print(f"Bonus: {bonus}")
        print(f"Gesamter oberer Teil: {summe_top + bonus}")
        print(self.paper_bottom)
        print()
        print(f"Gesamter oberer Teil: {summe_top + bonus}")
        print(f"Gesamter unterer Teil: {summe_bottom}")
        print(f"\nGesamtsumme: {summe_top + bonus + summe_bottom}")


	#!			-> Nachfrage nach lock (ask_lock()) 
    #?             Zeile 37??



#* MAIN
game = Game()
game.play()