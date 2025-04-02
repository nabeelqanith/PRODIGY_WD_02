n=input("enter your name : ")
a=['a','e','i','o','u','A','E','I','O','U']
sum=0
for  char in (n):
    for i in range(len(a)):
        if char==a[i]:
            sum+=i
    
if len(n)-sum<=2:
    print("veryy happy")
else:
    print("just happy")
    
    

n=input("enter your string :")
a=['a','e','i','o','u','A','E','I','O','U']
i=0
while i<len(n):
    if n[i] not in a:
        print(n[i],end="")
    i+=1 
    
a="abcdefghijklmnopqrstuvwxyz"
n=int(input("enter  number of rows :"))
s=0
for i in range(1,n+1):
    for j in range(i):
        print(a[s],end="")
        s+=1
    print()   
for i in range(n-1,0,-1):
    for j in range(i):
        print(a[s],end="")
        s+=1
    print()    
    
     