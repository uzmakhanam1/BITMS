#pattern


'''#X
def pattern(name):
    n = len(name)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print(name[i], end="")
            else:
                print(" ", end="")
        print()

user_name = input("Enter your name: ")
pattern(user_name)'''


'''#V
def pattern(name):
    n = len(name)
    for i in range(n):
        for j in range(n*2-1):
            if i == j or j == (n*2-2-i):
                print(name[i], end="")
            else:
                print(" ", end="")
        print()

user_name = input("Enter your name: ")
pattern(user_name)'''



#list


'''apple=[10,5,30]
print (apple)
apple[1]=300
print(apple)
apple[-1]=200
print(apple)
apple[-3]=100
apple[2]=(10,20,30)
print(apple)
apple[2:4]=(20,40)
print(apple)'''


#n-1 concept and STEP 
'''college=[10,20,30,40,50]
print(college[1])
print(college[-1])
print(college[1:7]) # if we dont have also no till seven index ie 6 values(n-1) it will display till it have ie 50
print(college[:])
print(college[-4:-1])# we cant write -1 first because it is grater than -4...also 50 is not printed because n-1 concept
print(college[3:-1])
print(college[1:])
print(college[:-1])
print(college[0:])
print(college[0:4:2])#here no n-1 concept ...because its STEP TYPE.also 50 is not coming beacause range we took till 4 ie n-1 =40 not 50.
'''

#user input(DYNAMIC)
'''uzma=[]
n=int(input('enter list size'))
for i in range(0,n):
    element=int(input('enter the elements'))# if we dont give int then it will default store as string 
    uzma.append(element)# append means  it will add at last
print(uzma)'''


#add,mul,max,min of  lists
'''siri=[1,2,3,4]
uzma=[5,6,7,8,10]
sanjana=siri+uzma
print(sanjana)
print(len(sanjana))
print(type(sanjana))
print(sanjana*3)
print(min(sanjana))
print(max(sanjana))'''

#sum
'''uzma=[1,2,3]
sum=0
for i in uzma:
    sum+=i
print(sum)'''


#print desired value like which end with 7
'''uzma=[10,25,37,40,57,65]
for i in uzma:
    if i%10==7:
        print(i)'''

#remove duplicate elements
'''uzma=[10,20,30,40,50,30,50]
siri=[]            #empty list
for i in uzma:
    if i not in siri:
        siri.append(i)  
print(siri)'''


#print common elements
'''yu=[10,20,30,40,50,100]
na=[60,70,80,90,100,20]
for i in yu:
    for j in na:
        if i==j:
            print(i)'''



#user input
'''
list=[]
n=int(input("enter list size"))
for i in range(0,n):
    e=int(input("enter the elements"))
    list.append(e)
print(list)'''




#5 values are stored in one list,,find which are prime number and leap year(2004,1996,17,10,85)
 
 
 
 
#tuple

'''apple=(1,2,3,4)
print(apple[1])
print(apple[-1])'''
'''apple[1]=100 # it does not suppor mutation
print(apple)'''




