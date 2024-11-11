class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return None

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        if 0 <= row < self.rows:
            del self.data[row]
            self.rows -= 1

    def delete_col(self, col):
        if 0 <= col < self.cols:
            for row in self.data:
                del row[col]
            self.cols -= 1

    def add_row(self, row):
        if 0 <= row <= self.rows:
            self.data.insert(row, [0] * self.cols)
            self.rows += 1

    def add_col(self, col):
        if 0 <= col <= self.cols:
            for row in self.data:
                row.insert(col, 0)
            self.cols += 1


tab = Table(3, 3)
tab.set_value(0, 0, 50)
tab.set_value(1, 1, 60)
tab.set_value(2, 2, 70)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(3)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
