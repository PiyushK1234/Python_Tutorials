class Student:
    collegeName ="ABC"
    def __init__(self, name , marks):
        self.name = name
        self.marks= marks

s1= Student("Piyush",98);
del s1
print(s1)