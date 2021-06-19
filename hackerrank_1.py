# to check the number that it is weird or not weird in the case of even or odd.

n=int(input('Enter the number:- '))
if n%2==0:
    if 2>=n>=5:
        print('Not Weird')
    if n==4:
        print('Not Weird')
    if 6>=n>20:
        print('Weird')
    if n==18:
        print('Weird')
    if n>=20:
        print('Not Weird')
else:
    print('weird')