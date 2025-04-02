n=int(input("enter number of elements in list :"))
a=[]
for i in range(n):
    element=int(input("enter element :"))
    a.append(element)
print(a)
b=[]
for i in (a):
    if i not in b:
        b.append(i)
print(b)

n=int(input("enter number of elemnts in list :"))
a=[]
for i in range(n):
    element=int(input("enter element :"))
    a.append(element)
print(a)
m1=-1
m2=0
for i in (a):
    if i>m1:
        m2=m1
        m1=i
    elif i<m2 and i!=m1:
        m2=i
print(f"{m2} is second largest element ")

n=int(input("enter number of elemnts in list :"))
a=[]
for i in range(n):
    element=int(input("enter element :"))
    a.append(element)
print(a)
m=0
for i in a:
    if i>m:
        m=i
print(f"{m} is largest element")
a.remove(m)
print(a)
b=0
for i in a:
    if i>b:
        b=i
print(f"{b} is second largest")


set1={1,2,3,4,5}
set2={3,4,5,6,7}



    
    
