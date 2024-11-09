class Balance:
    def __init__(self):
        self._right_weight = 0
        self._left_weight = 0

    def add_right(self, weight):
        self._right_weight += weight
        
    def add_left(self, weight):
        self._left_weight += weight  
    
    def result(self):
        if self._right_weight == self._left_weight:
            return "=" 
        elif self._right_weight > self._left_weight:
            return "R"
        elif self._right_weight < self._left_weight:
            return "L"

balance = Balance()
balance.add_right(2)
balance.add_left(3)
balance.add_left(1)
print(balance.result())
balance.add_right(3)
print(balance.result())
balance.add_left(1)
print(balance.result())
