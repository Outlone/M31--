class OddEvenSeparator:
    def __init__(self):
        self._even_numbers = []
        self._odd_numbers = []
        
    def add_number(self, number):
        if number % 2 == 0:
            self._even_numbers.append(number)
        else:
            self._odd_numbers.append(number)
            
    def even(self):
        return self._even_numbers
    
    def odd(self):
        return self._odd_numbers
        
separator = OddEvenSeparator()
separator.add_number(2)
separator.add_number(5)
separator.add_number(6)
separator.add_number(9)
separator.add_number(10)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
