class A:
    def feaure1(self):
        print("feature1 working")

    def feature2(self):
        print("feature2 is working")

class B():

    def feaure3(self):
        print("feature3 working")

    def feature4(self):
        print("feature4 working")

class C(A,B):

    def feature5(self):
        print("Feature5")

b1 = B()
b1.feaure1()
b1.feature2()
b1.feaure3()
b1.feature4()

c1 = C()
