class newStudent:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            laptop = "HP"
            processor = "i5"
            ram = 8


lap1 = newStudent.Laptop()
