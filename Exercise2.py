#Show the student grade based on the inserted data
def evaluation(grade):
    if grade >= 9:
      note = 'A'
    elif grade >= 7 and grade < 9:
        note = 'B'
    elif grade >=5 and grade < 7:
        note = 'D'
    else:
        note = 'F'
    return note

grade = int(input('Enter your note: '))
student_grade = evaluation(grade)
print(student_grade)
    

             