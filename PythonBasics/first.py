l2 = [1,3,5,6,1,5,1,8];


for x in l2:
  if(x==1):
    l2.remove(1);
 

print(l2)


tup = (1,2,3445,56,67,89,9,0)
tup2 =(2,)
print(tup2)
print(type(tup2))



l3=[1,2,1,4]
l4 =l3.copy()
l4.reverse()
print(l3==l4)


s1={1,3,5,71,54,1,4,3}
print(s1)
s1.add(55)
print(s1)
for x in range(2,10,2):
  print(x)



def sum(a,b):
  res = a+b
  return res

print(sum(12,33))