def evaluation(exam1,exam2, exam3):

    final_grade = (exam1 * 0.4) + (exam2 * 0.4) + (exam3 * 0.2) 
    return final_grade

student_grade = evaluation(7,8,9)
print(student_grade)
