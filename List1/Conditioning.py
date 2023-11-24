#First conditioning in Python

#1st step function name
#2nd define variables
#3 define parameters
#4 define conditioning 

def evaluation(grade,frequency):
    if grade >= 7 and frequency >= 0.75:
        approved = "Student approved"
    else:
        approved = "Student not approved"
    return(approved)

grade = float(input('Type your grade/note:'))
frequency = float(input('Enter your frequency>'))

student =   evaluation(grade, frequency)
print(student)



