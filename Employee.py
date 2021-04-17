re=eval(input('Enter the salary of the employee:- '))
st=int(input('Enter the year of the employee:- '))
if st>=5:
    ls=re*st/100
    print(f'The cash given to the employee:- {re+ls}')
    print('The bonus is given to the employee is :-' ,ls)
else:
    print('sorry ! you are new employee')