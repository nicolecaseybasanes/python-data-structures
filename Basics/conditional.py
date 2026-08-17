student_name = input("Student Name: ")

try:
    student_score = int(input("Student Score: "))


    if 90 <= student_score <= 100:
            print("Grade: A")
    elif  80 <= student_score <=89:
            print("Grade:B")
    elif 70 <= student_score <=79:
            print("Grade:C")
    elif  61 <= student_score <=69:
            print("Grade:D")
    elif student_score <=60:
            print("Grade: F")
    else:
        print("Invalid Grade")

except ValueError:
    print("Invalid Grade")
