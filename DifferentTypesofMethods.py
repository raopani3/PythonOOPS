class Students:
    SchoolName = "Phanindra University"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchoolName(cls):
        return cls.SchoolName

    @staticmethod
    def getInfoSample():
        print("Nothing to do with any other things, this is static method")


s1 = Students(100, 67, 89)
s2 = Students(99, 98, 45)

print(s1.avg())
print(s2.avg())

print(Students.SchoolName)
Students.getInfoSample()
