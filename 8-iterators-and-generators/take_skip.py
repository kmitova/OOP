class TakeSkip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration
        current = self.iterations * self.step
        self.iterations += 1
        return current


numbers = TakeSkip(10, 5)
for number in numbers:
    print(number)

