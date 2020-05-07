num = [7, 8, 9, 10]

it = iter(num)

print(it.__next__())
print(next(it))


class Topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1
            return val

        else:
            raise StopIteration


c1 = Topten()

print(next(c1))

for i in c1:
    print(i)

