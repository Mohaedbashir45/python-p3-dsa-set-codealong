class MySet:
    def __init__(self, input_list=None):
        self.dictionary = {}
        if input_list is not None:
            for value in input_list:
                self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        if value in self.dictionary:
            del self.dictionary[value]
        return self

