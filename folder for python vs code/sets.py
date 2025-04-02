rows=int(input("Enter number of rows :"))
columns=int(input("Enter number of columns :"))
a=[]
for i in range(rows):
    b=[]
    for j in range(columns):
        element=int(input(f"element {i}{j}:"))
        b.append(element)
    a.append(b)
print(a)
for i in range(rows):
    sum=0
    for j in range(columns):
        sum+=a[i][j]
    a[i].append(sum)
print(a)
x=[]
f=0
for i in range(rows):
    s=0
    for j in range(columns):
        s+=a[j][f]
    f=f+1
    x.append(s)
a.append(x)
print(a)

                            