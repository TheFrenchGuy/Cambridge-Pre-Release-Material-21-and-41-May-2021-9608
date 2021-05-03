def add_student_file():
    keepRecord = True
    f = open("StudentStorage.txt", "a")
    while keepRecord:
        studentID_correct = False
        studentID = ""
        while studentID_correct == False:
            print("A student ID should be 2 Capital letters followed by 4 digits")
            tempstudentID = input("Please input the student ID")
            if tempstudentID[0:2].isupper():
                if tempstudentID[2:6].isnumeric() and len(tempstudentID) == 6 :
                    studentID = tempstudentID
                    print("The student recorded is: " + studentID)
                    studentID_correct = True

        studentEmail_correct = False
        studentEmail = ""

        while not studentEmail_correct:
            print("An email addresss should have an @ and finish with . domain identifier")
            tempstudentEmail = input("Please input the student email address")

            if "@" and "." in tempstudentEmail:
                posemail = 0
                posedot = 0
                for i in range(len(tempstudentEmail)):

                    if tempstudentEmail[i] == "@":
                        posemail = i + 1
                        print(posemail)
                    if tempstudentEmail[i] == ".":
                        posedot = i + 1
                        print(posedot)
                if posemail < posedot:
                    studentEmail = tempstudentEmail

                    print("Email recorded is:" + studentEmail)

                    studentEmail_correct = True




        studentDOB_correct = False
        studentDOB = ""

        while not studentDOB_correct:
            temp_studentDOB = input("Please input the student date of birth in the format DDMMYY")

            if int(temp_studentDOB[0:2]) <= 31 and int(temp_studentDOB[0:2]) >= 1 and int(temp_studentDOB[2:4]) >= 1 and int(temp_studentDOB[2:4]) <= 12 and len(temp_studentDOB) == 6 :
                studentDOB = temp_studentDOB
                print("student DOB is: " + studentDOB)
                studentDOB_correct = True
            else: print("The student date of birth should be in DDMMYY")



        studentFormat = studentID + studentEmail + studentDOB + "\n"

        f.write(studentFormat)


        add_to_record = input("Keep adding students to the record? [Y/N]")

        if add_to_record == "Y":
            keepRecord = True
        if add_to_record == "N":
            keepRecord = False

    f.close()


def find_student_from_file():
    f = open("StudentStorage.txt", "r")
    studentID_correct = False
    studentID = ""
    while studentID_correct == False:
        print("A student ID should be 2 Capital letters followed by 4 digits")
        tempstudentID = input("Please input the student ID")
        if tempstudentID[0:2].isupper():
            print("isUpper")
            if tempstudentID[2:6].isnumeric() and len(tempstudentID) == 6:
                studentID = tempstudentID
                print("The student recorded searched is: " + studentID)
                studentID_correct = True

    listofLines = f.readlines()

    found_email = 0
    for line in listofLines:
        if line[0:6] == studentID:
            found_email += 1
            print(line.strip()[6:][: -6])
        else: found_email += 0

    if not found_email >= 1:
        print("\n")
        print("There was no student with that Student ID and no email was attached to it")

    f.close()
def find_student_substring():
    f = open("StudentStorage.txt", "r")

    searchString = input("Search if substring is in the record")

    listofLines = f.readlines()

    for line in listofLines:
        if searchString in line:
            print(line.strip())


add_student_file()
#find_student_from_file()

#find_student_substring()