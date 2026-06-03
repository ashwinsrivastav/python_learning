class teacher:
    def __init__(self,subject):
        self.subject=subject
        if self.subject=="maths":
            m1=self.maths()
        elif self.subject=='science':
            s1=self.science()
        elif self.subject=="all":
            a1=self.all()
        else:
            print("subject invalid")
            
    class maths:
        def __init__(self):
            print("list of all the maths students")
        def total(self):
            print("24")
    class science:
        def __init__(self):
            print("list of all the science students")
        def total(self):
            print("23")
    class all(maths,science):
        def __init__(self):
            teacher.science()
            teacher.maths()
            teacher.maths.total(self)
            teacher.science.total(self)

            

#s1=teacher(input("enter the subject:- "))
a=[1,3,4,45,5,6,6]
it=iter(a)
print(it.__next__())
print(it.__next__())
print(it.__next__())

        