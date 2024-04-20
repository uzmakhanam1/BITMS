names="uzmakhanam"
'''print(names)
print(names[:])
print(names[2:])
print(names[-1:])
print(names[-5:-1])
print(names[::-1])
print(names[::-3])'''
'''j=0
for i in range(len(names)):
    res=names[j]+names[j+1]+'-'
    j=j+3
    print(res,end="")'''
    
'''name="uzmakhanam"
vowels="aeiou"
res=[char for char in name if char in vowels]
print(res)'''


'''name="uzmakhanam"
vowels="aeiou"
res=[char for char in name if char  not in vowels]
print(res)'''



#inbuild methods

'''list="uzma khanam"
print(list.upper())
print(list.capitalize())
print(list.title())
print(list.strip())'''

#file methods

'''uz=open("uz.txt","r")
print(uz.read())'''




#exeptional handling

'''print(dir(locals()['__builtins__']))
'''


try:
    num=0
    deno=0
    result=num/demo
    print(result)
except:
    print("exception")


      