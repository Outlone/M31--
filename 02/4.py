class MaxStat:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def result(self):
        return max(self.numbers) if self.numbers else None

class MinStat:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def result(self):
        return min(self.numbers) if self.numbers else None

class AverageStat:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def result(self):
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)

values = [10, 22, 40, 6]

maxs = MaxStat()
mins = MinStat()
average = AverageStat()
for v in values:
    maxs.add_number(v)
    mins.add_number(v)
    average.add_number(v)

print(maxs.result(), mins.result(), '{:<05.3}'.format(average.result()))
