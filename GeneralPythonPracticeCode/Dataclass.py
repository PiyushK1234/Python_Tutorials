from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name:str
    age:int
    friends:list[str]


piyush: Person = Person("Piyush",25,["Kumar","Singh"])
print(piyush)
piyush1:Person =Person("Aman",29,["Kumar","Singh"])
print(piyush1)
#piyush.name="fghkj"
print(piyush)
print(piyush1)


print("-------------------------------WithOut Dataclasses--------------------------------------------------")

class Person1:
    def __init__(self,name , age , li):
        self.name = name
        self.age = age
        self.li=li

    def __str__(self):
        return f'Person(name ={self.name}, age={self.age}, friends={self.li})'
        


piyush3: Person1 = Person1("Piyush",25,["Kumar","Singh"])
print(piyush3)