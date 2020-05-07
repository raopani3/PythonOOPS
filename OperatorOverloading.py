class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

    def __gt__(self, other):
        r1 = self.m1 + other.m2
        r2 = self.m2 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(87, 90)
s2 = Student(89, 89)

s3 = s1 + s2
print(s3)
print(s1 > s2)

print(s1)
