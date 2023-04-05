
num1=int(input("what is the first number"))
num2=int(input("what is the second number"))
choice=int(input("what do you want to do, 1.addition, 2.subtraction, 3.multiplication, 4.division, 5.modulus"))
if(choice==1):
    result=num1+num2
    print(result)
elif(choice==2):
    result=num1-num2
    print(result)
elif(choice==3):
    result=num1*num2
    print(result)
elif(choice==4):
    result=num1/num2
    print(result)
elif(choice==5):
    result=num1%num2
    print(result)
else:
    print("error")
