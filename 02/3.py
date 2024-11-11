class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f"{str(self.month).zfill(2)}.{str(self.day).zfill(2)}.{self.year}"

class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f"{str(self.day).zfill(2)}.{str(self.month).zfill(2)}.{self.year}"

american = AmericanDate(2024, 11, 12)
european = EuropeanDate(2022, 5, 6)
print(american.format())
print(european.format())
