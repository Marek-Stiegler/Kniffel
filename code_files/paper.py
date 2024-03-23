
class Paper():
    def __init__(self) -> None:
        self._list_values = []
        self._list_options = []
        self._list_combinations = []
        
    def set_list_values(self, list_values:list) -> None:
        self._list_values = list_values
    
    def add_list_fixed(self, index:int) -> None:
        if self._list_fixed[index] == None:
            self._list_fixed[index] = self._list_options[index]
            return True
        else:
            return False
       
    def get_list_options(self) -> list:
        return self._list_options
    
    
    def get_points(self) -> int:
        return sum([v for v in self._list_fixed if v != None])
    
    def __str__(self) -> None:
        text = '\n'
        for i in range(len(self._list_combinations)):
            text += self._list_combinations[i]
            
            if self._list_fixed[i] != None:
                text += str(self._list_fixed[i]) + '\n'
            else: 
                text +=  f'({str(self._list_options[i])}) \n' 
        return text
        

class Paper_top(Paper):
    def __init__(self) -> None:
        super().__init__()
        self._list_combinations = ['Ones: ', 'Twos: ', 'Threes: ', 'Fours: ', 'Fives: ', 'Sixes: ']
        self._list_fixed = [None for _ in range(6)]

    def evaluate_options(self):
        for number in range(1,7):
            counter = 0
            for dice in self._list_values:
                if dice == number:
                    counter += number
            self._list_options.append(counter)
            



class Paper_bottom(Paper):
    def __init__(self) -> None:
        super().__init__()
        self._list_combinations = ['Three of a Kind: ', 'Four of a Kind: ', 'Full House: ', 'Small Straight: ', 'Large Straight: ', 'Chance: ', 'Kniffel: ']
        self._list_fixed = [None for _ in range(7)]
    
    def evaluate_options(self):
        
        def cal_three(dices:list) -> int:
            for i in range(1,7):
                if dices.count(i) >= 3:
                    return sum(dices)
            return 0

        def cal_four(dices:list) -> int:
            for i in range(1,7):
                if dices.count(i) >= 4:
                    return sum(dices)
            return 0

        def cal_full_house(dices:list) -> int:
            count = [0,0,0,0,0,0] #number of ones, twos ...
            tree = False
            two = False
            for dice in dices:
                count[dice-1] += 1
            for i in count:
                if i == 3:
                    tree = True
                if i == 2: 
                    two = True
            if two and tree:
                return 25
            else:
                return 0

        def cal_small_straight(dices: list) -> int:
            dices.sort()
            possible_small_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
            for possible_small_straight in possible_small_straights:
                is_small_straight = True
                for dice in possible_small_straight:
                    if dice not in dices:
                        is_small_straight = False
                        break
                if is_small_straight:
                    return 30
            return 0

        def cal_large_straight(dices: list) -> int:
            dices.sort()
            possible_large_straights = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
            for possible_large_straight in possible_large_straights:
                is_large_straight = True
                for dice in possible_large_straight:
                    if dice not in dices:
                        is_large_straight = False
                        break
                if is_large_straight:
                    return 40
            return 0

        def cal_chance(dices:list) -> int:
            return sum(dices)

        def cal_kniffel(dices:list) -> int:
            for dice in dices:
                if dice != dices[0]:
                    return 0
            return 50
    
        self._list_options.append(cal_three(self._list_values))
        self._list_options.append(cal_four(self._list_values))
        self._list_options.append(cal_full_house(self._list_values))
        self._list_options.append(cal_small_straight(self._list_values))
        self._list_options.append(cal_large_straight(self._list_values))
        self._list_options.append(cal_chance(self._list_values))
        self._list_options.append(cal_kniffel(self._list_values))

        








#------------Main-----------

# l = [1,5,6,2,1]

# p_top = Paper_top()
# p_bottom = Paper_bottom()

# p_top.set_list_values(l)
# p_bottom.set_list_values(l)


# while True:
  
#     p_top.evaluate_options()
#     p_bottom.evaluate_options()    
#     v_top = p_top.add_list_fixed(int(input()))
#     v_bottom = p_bottom.add_list_fixed(int(input()))
  
#     print(v_top, v_bottom)
  
#     print(p_top)
#     print(p_bottom)
    
#     print(p_top.get_points())
#     print(p_bottom.get_points())

