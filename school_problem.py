# school problem
ls=eval(input('enter the marks of the student:- '))
if ls>80:
    print('very good the student is getting A grade')
elif ls<80 and ls>60 :
    print('the student is getting B grade')
elif ls<60 and ls>50:
    print('the student is getting C grade')
elif ls<50 and ls>45:
    print('the student is getting D grade')
elif ls<45 and ls>25:
    print('the student is getting E grade')
else:
    print('the student is very poor and getting F grade')