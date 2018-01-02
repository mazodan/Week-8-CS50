class Dictionary:
    def __init__(self):
        # Declares an empty set
        self.words = set()

    def load(self, dictionary):
        file = open(dictionary, "r")
        for line in file:
            self.words.add(line.rstrip('\n'))
        file.close()
        return True

    def check(self, word):
        return word.lower() in self.words

    def size(self):
        return len(self.words)

    def unload(self):
        return True
