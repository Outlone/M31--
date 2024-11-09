class BigBell:
    def __init__(self):
        self.cycle = "ding"

    def sound(self):
        print(self.cycle)
        if self.cycle == "ding":
            self.cycle = "dong"
        else:
            self.cycle = "ding"
            
# Ваш код

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
