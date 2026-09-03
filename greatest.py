a1=int(input("Enter Your Number: "))
a2=int(input("Enter Your Number: "))
a3=int(input("Enter Your Number: "))
a4=int(input("Enter Your Number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print(a1,"is greater number")
elif(a2>a1 and a2>a3 and a2>a4):
    print(a2,"is greater number")
elif(a3>a1 and a3>a2 and a3>a4):
    print(a3," is greater number")
else:
    print(a4,'is greater number')








marks1=int(input("Enter Marks : "))
marks2=int(input("Enter Marks : "))
marks3=int(input("Enter Marks : "))

total_percentage=(100*(marks1+marks2+marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Passed",total_percentage)
else:
    print("You are Failed In Exam ",total_percentage)








p1="Make A Lote Of Money"
p2="buy Now"
p3="Subscribe This"
p4="click this"

a=input("spam Detecter: ")

if((p1 in a) or  (p2 in a) or (p3 in a) or  (p4 in a)):
    print("these are spam messages")
else:
    print("not a spam message")









a=input("Enter Username: ")
if(len(a)<10):
    print("username should not be less then 10 charecters")
else:
    print("username is good")








li=["anand", "amar","shivakumar","shreedhar","akshay","santosh"]
name=input("Enter Your Name: ")
if(name.lower() in li):
    print("Name is Existed")
else:
    print("Name is Not Defined In List")