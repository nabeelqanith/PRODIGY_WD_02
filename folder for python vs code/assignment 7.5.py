m=int(input("enter number of rows:"))
n=int(input("enter number of colummns:"))
a=[]
for i in range(m):
    r=[]
    for j in range(n):
        element=int(input(f"enter element[{i}{j}] :"))
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
    

    
m=int(input("enter nuumber of rows :"))
n= int(input("enter number of colummns:"))
a=[]
for i in range(m):
    r=[]
    for j in range(n):
        element=int(input(f"enter element[{i}{j}]: "))
        r.append(element)
    a.append(r)
print (a)

sum=0
for i in range(m):
    sum+=a[i][i]
print(sum)
        
m1=int(input("enter number of rows for matrix 1:"))
n1=int(input("enter number of columns for matrix 1:"))
a=[]
for i in range(m1):
    r=[]
    for j in range(n1):
        element=int(input(f"enter element[{i}{j}] :"))
        r.append(element)
    a.append(r)
print(a)

m2=int(input("enter number of rows for matrix 2 :"))
n2=int(input("enter number of columns for matrix 2 :"))
b=[]
for i in range(m2):
    z=[]
    for j in range(n2):
        p=int(input(f"enter element[{i}{j}] :"))
        z.append(p)
    b.append(z)
print(b)

if m1==m2 and n1==n2:
    for i in range(m1):
        for j in range(n1):
            print(a[i][j]+b[i][j],end=" ")
            print()
        
        
        
        
        
        
        