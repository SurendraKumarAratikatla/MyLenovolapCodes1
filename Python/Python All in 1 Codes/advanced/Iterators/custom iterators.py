class even:
    def __init__(self,max):
        self.n = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            value = self.n
            self.n += 2
            return value

        else:
            raise StopIteration

numbers = even(10)

i = iter(numbers)

print(next(i))
print(next(i))
print(next(i))