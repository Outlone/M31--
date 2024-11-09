class MinMaxWordFinder:
    def __init__(self):
        self.words_by_length = {}
        self.shortest_length = float('inf')
        self.longest_length = float('-inf')

    def add_sentence(self, sentence):
        words = sentence.split()
        for word in words:
            word = word.strip()
            if word:
                length = len(word)
                if length not in self.words_by_length:
                    self.words_by_length[length] = []
                self.words_by_length[length].append(word)
                self.shortest_length = min(self.shortest_length, length)
                self.longest_length = max(self.longest_length, length)

    def shortest_words(self):
        return sorted(self.words_by_length[self.shortest_length])

    def longest_words(self):
        return sorted(set(self.words_by_length[self.longest_length]))
        
finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('defin qwert')
finder.add_sentence('world')
finder.add_sentence('asdf')
finder.add_sentence('asd')
finder.add_sentence('def')
print(' '.join(finder.shortest_words()))
