StudentClass = []




def input_class():
    input_student = True
    while input_student:
        list = []
        student_name = input("input the student name: ")
        student_email_address = input("input the student email address: ")
        student_dob = input("input the student date of birth: ddmmyyyy")
        student_left = input("is the student still in school? [Yes/No]")
        student_format =  str(student_name + "*" + student_email_address + "*" + student_dob + "*" + student_left + "!")
        student_id = input("input the student ID")
        student_tutorID = input("input the Tutor ID")
        list.append(student_name)
        list.append(student_email_address)
        list.append(student_dob)
        list.append(student_left + "!")
        list.append(student_id)
        list.append(student_tutorID)
        StudentClass.append(list)
        print(StudentClass)
        keep = input("Keep adding [Y/N]")

        if keep == "Y":
            input_student = True
        if keep == "N":
            input_student = False


def display_class():
    print("<Student Name> * <Email Address> * <Date of Birth> * <Current Student> * <Student ID> * <Tutor ID>")
    for index in range(0, len(StudentClass)):
        if "No!" in str(StudentClass[index][3]):
            print("Record Deleted")
        else :
            print(str(StudentClass[index]) + "\n")

def share_birthday(month):
    print("Class dispaly of all of the students that share the same birth month")
    print("<Student Name> * <Email Address> * <Date of Birth> * <Current Student> * <Student ID> * <Tutor ID>")
    for index in range(0, len(StudentClass)):
        splString = str(StudentClass[index][2])
        if month == splString[2:4]:
            print(str(StudentClass[index]) + "\n")
        #else:
        #    print(splString[2:4])
input_class()

print("Class display of all of the current students")
display_class()

share_birthday(str(input("Please enter the birthmonth your searching student from e.g mm")))




