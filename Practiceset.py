# print Multiplication table
n=int(input("Enter A number:"))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


# find the name Which Starts with the S letter
li=["Anand","Amar",'Shivu','Shreedhar','Santosh']
for name in li:
    if(name.startswith('S')):
        print(name)

# print the Multipliaction Table using While Loop
n=int(input('Enter A number: '))
i=1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i+=1


# Check Given Number Is Prime Or non Prime Number
n=int(input('Enter A number: '))
for i in range(2,n):
    if(n%2)==0:
        print("Given Number Is not A prime Number")
        break
    else:
        print("Given Number Is Prime Number ")


# Find The Sum of The Given Value by Using While Loop ex:1,2,3,4=10
n=int(input('Enter A Number: '))
i=1
sum=0
while(i<=n):
    sum +=i
    i+=1
print(sum)

# Find The Factorial  value of Given Number
n=int(input('Enter A Numerb: '))
i=1
fact=1
while(i<=n):
    fact *=i
    i+=1
print(fact)


# using for loop
n=int(input('Enter A Number: '))
fact=1
for i in range(1,n+1):
        fact*=i
print(fact)

# * Pyramid Generate as following Below
'''
    *
   ***
  *****
'''

n=int(input("Enter A number:"))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")

'''
*
**
***
'''
n=int(input("Enter A Number:"))
for i in range(1,n+1):
    print('*'*i,end='')
    print("")


'''
***
* *
***
'''
n=int(input('Enter A number: '))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")

#  print reverse Multiplication table
n=int(input('Enter A number'))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")