# Take two int values from user and print greatest among them.
re=int(input('Enter the value:- '))
st=int(input('Enter other value:- '))
if re>st :
    print(f'the greatest value is {re}')
elif st>re:
    print(f'The greatest value is {st}')
else:
    print(f'The both values is equal {re}')
