'''#nested conditional with help of INTENTATION
email="sadiuzma2gmail.com"
pwd=12345
uemail=str(input("enter the email"))
upwd=int(input("enter the password"))
if(email==uemail):
    if(pwd==upwd):
        print("login success")
    else:
        print("login failed due to password")
else:
    print("login failed due to incorrect email")'''
    



'''#elif
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
if(num1>num2):
    printf(num1,"id greater")
elif(num1<num2):
    print(num2,"is greater")
else:
    print("num1 and num2 are equal")'''



'''#ternary operator (here firt output comes then the condition for that output)
a=50
b=10
c=-15
print('a' if a>b and a>c else 'b' if b>c else 'c')'''




'''a=100
b=80
c=700
d=5000
e=20000
print('a' if a>b and a>c and a>d and a>e else 'b' if b>c and b>d and b>e else 'c' if c>d and c>e else 'd' if d>e else 'e')'''


'''#name in knnada
print(chr(3209)+chr(3228)+chr(3246))'''



'''#lemon 21 lemons
a=int(input("enter the no of lemons:"))
print('extra by{}'.format(a-21) if a>21 else 'less by{}'.format(21-a) if a<21 else 'sufficient no of lemons')'''


'''print(chr(3206)+chr(3205))
print(ord('a'))
for i in range(ord('A'),ord('Z')):
    print(ord(chr(i)),end=' ')'''


#pattern problems

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()'''
    
    
'''for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()'''


'''for i in range(65,91):
    for j in range(65,i+1):
        print(chr(i),end=' ')
    print()'''
    
    
'''for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=' ')
    print()'''


'''for i in range (1,11):
    print((i/10),end=' ')'''


#functions

'''a=-5
print(abs(a))
print(pow(2,3))'''


#user define
'''def uzma():
    n=366
    if(n==366):
        print('it is leap year')
    else:
        print('it is not a leap year')
uzma()'''
    
    
'''def table():
    for i in range(1,11):
        print(i,"*10=",i*10)
table()'''


'''#leap year----see explation in notes
def leap():
    n=int(input("enter the year"))
    if(n%4==0 and n%400==0):
        print("leap year")
    else:
        print("not leap year")
leap()'''
    


