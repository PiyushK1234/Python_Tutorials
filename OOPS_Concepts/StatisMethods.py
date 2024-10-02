class Students:
    def __init__(self,name, marks):
        self.name= name 
        self.marks= marks
    
    def avg(self):
        return sum(self.marks)/len(self.marks)
    
    @staticmethod
    def hello(name):
        print("Hello",name)


s2 =Students ("Piyush",[98,99,97])
print(s2.avg())
s2.hello(s2.name)