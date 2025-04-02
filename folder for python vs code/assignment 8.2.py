m=int(input("enter nnumber of rows :"))
n=int(input("enter number of columns :"))
a=[]
for i in range(m):
    r=[]
    for j in range(n):
        element=int(input(f"enter element [{i}{j}] :"))
        r.append(element)
    a.append(r)
print(a)
for i in range(m):
    for j in range(n):
        if i>=j:
            print(a[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
    
m=int(input("enter number of rows :"))
n=int(input("enter number of columns :"))
a=[]
for i in range(m):
    r=[]
    for j in range(n):
        element=int(input(f"enter elements [{i}{j}] :"))
        r.append(element)
    a.append(r)
print(a)
sum=0
for i in range(m):
    sum+=a[i][i]
print(sum)


strecord=[]
name=input("enter name:")
roll =int(input("enter roll number :"))
marks=[]
s=0
for i in range (5):
    r=int(input("enter marks :"))
    marks.append(r)
    s+=r
percentage=(s/500)*100
strecord.append([name,roll,marks,percentage])  
print(strecord)  
