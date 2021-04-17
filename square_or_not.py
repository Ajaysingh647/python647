# Take values of length and breadth of a rectangle from user and check if it is square or not.

ln=int(input('Enter the length:- '))
wt=int(input('Enter the breadth:- '))
if (ln==wt):
    print("it is square")
    ar=ln*ln
    print('the area of the square is:- ' ,ar)
    vl=4*wt
    print('And the volume is:- ' ,vl)
else:
    print('it is not square')
    print('the area of the rectangle is:- ',ln*wt)
    print('The perimeter of the rectangle is:- ' ,2*(ln+wt))