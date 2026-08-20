student_name = input("Student Name: ") #user name input

try:
    student_score = int(input("Student Score: ")) #user input score


    if 90 <= student_score <= 100:
            print(student_name,"received Grade A") #prints if score is 90-100
    elif  80 <= student_score <=89:
            print(student_name,"received Grade B") #prints if score is 80-89
    elif 70 <= student_score <=79:
            print(student_name,"received Grade C") #prints if score is 70-79
    elif  61 <= student_score <=69:
            print(student_name,"received Grade D") #prints if score is 61-69
    elif student_score <=60:
            print(student_name,"received Grade F") #prints if score is below 60
    else:
        print("Invalid Grade") #prints if score input is not an integer

except ValueError:
    print("Invalid Grade") #prints if score input is invalid




