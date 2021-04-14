#. Remove all Characters in a String except alphabet (user defined)

r='Ajay singh 12861@*7'
s=''
for i in r:
    if(ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        s+=i
print(f'Alphabets in string are:{s}')



#. Remove all Characters in a String except alphabet (given bythe user)
r=input('Enter the elements:- ')
s=''
for i in r:
    if(ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        s+=i
print(f'Alphabets in string are:{s}')



