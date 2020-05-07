from demo import Calculator


class childimps(Calculator):
    num2 = 100

    def __init__(self):
        Calculator.__init__(self, 2, 100)

    def haha(self):
        return self.num + self.num2 + self.addNumbers()


child = childimps()
nwe = child.haha()
print(nwe)

