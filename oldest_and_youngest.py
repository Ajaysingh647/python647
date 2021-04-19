# Take input of age of 3 people by user and determine oldest and youngest among them.
a=eval(input('Enter age of the person:- '))
b=eval(input('Enter another person,s age:- '))
c=eval(input('Enter another age:- '))
if a>b and b>c:
    print('The olest age is :-' ,a)
    print('The youngest age is :-' ,c)
elif b>a and a>c:
    print('The olest age is :-' ,b)
    print('The youngest age is :- ' ,c)
else:
    print('The olest age is :-' ,c)
    print('The youngest age is :-' ,a)
