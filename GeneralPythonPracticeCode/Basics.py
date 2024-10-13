thislist = ["apple", "banana", "cherry"]
l=thislist.pop(-2)
print(thislist)
print(l)




list1:int=[1,2,3,45,63,322,12,243,5,6]
result= [num for num in list1 if num>10]
print(result)


l1 =[1,2,3,4]
l2 = l1.copy()
print(l1)
print(l2)

l1[0]=0
print(l1)
print(l2)

class Payloads:

   @staticmethod
   def postpayload():
      return {
          "id": 7,
          "title": "Piyush Kumar",
          "dueDate": "2024-10-13T05:20:08.603Z",
          "completed": True
}


print(Payloads.postpayload())