#collage attendence problem
hc=int(input('Enter the classes held in the campus:- '))
ac=int(input('Enter the classes attend by the student:- '))
pc=ac/hc*100
if pc>75:
    print(f'the student is getting:- {pc} attendence and able to sit down in the EXAM ')
    if hc==ac:
        print('CONGRATULATION! you are qualified for tour for NEW DELHI(free of cost)')
else:
        print(f'the student is getting:- {pc} attendence and does not able to sit in the EXAM')