class Student:
    collegeName ="ABC"
    def __init__(self, name , marks):
        self.name = name
        self.marks= marks

    def Welcome(self):
        print("Hello",self.name)

    def Marks(self):
        return self.marks
    

s1= Student("piyush",96);
s1.Welcome();
print(s1.Marks())
print(s1.collegeName)

print("------------------------------------------------------------")

class Students:
    def __init__(self,name, marks):
        self.name= name 
        self.marks= marks
    
    def avg(self):
        return sum(self.marks)/len(self.marks)


s2 =Students ("Piyush",[98,99,97])
print(s2.avg())