class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
        self.current_line = []

    def add_word(self, word):
        if sum(len(w) for w in self.current_line) + len(self.current_line) + len(word) <= self.width:
            self.current_line.append(word)
        else:
            self.words.append(' '.join(self.current_line))
            self.current_line = [word]

    def end(self):
        if self.current_line:
            self.words.append(' '.join(self.current_line))
        for line in self.words:
            print(line.rjust(self.width))

class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
        self.current_line = []

    def add_word(self, word):
        if sum(len(w) for w in self.current_line) + len(self.current_line) + len(word) <= self.width:
            self.current_line.append(word)
        else:
            self.words.append(' '.join(self.current_line))
            self.current_line = [word]

    def end(self):
        if self.current_line:
            self.words.append(' '.join(self.current_line))
        for line in self.words:
            print(line)

lp = LeftParagraph(8)
lp.add_word('adhh')
lp.add_word('xim')
lp.add_word('so')
lp.add_word('ggbeel')
lp.add_word('z')
lp.add_word('stuff')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('adhh')
rp.add_word('xim')
rp.add_word('so')
rp.add_word('ggbeel')
rp.add_word('z')
rp.add_word('stuff')
rp.end()
