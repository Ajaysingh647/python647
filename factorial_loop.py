# to find the factorial of any number given by the user
n=int(input('Enter the number from where you want to find the factorial:- '))
fact=1
for i in range(1,n+1):
    fact=fact*i
print('the factorial is:- ',fact)