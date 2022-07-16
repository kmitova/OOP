class sequence_repeat:
    def __init__(self, string, number):
        self.string = string
        self.number = number
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == self.number:
            raise StopIteration
        symbol = self.string[self.pointer % len(self.string)]
        self.pointer += 1
        return symbol


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
