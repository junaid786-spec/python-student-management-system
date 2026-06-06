students =[]
while True:
    print("==STUDENTS MANAGEMENT SYSTEM==")
    print("1:ADD STUDENT")
    print("2:SHOW STUDENT")
    print("3:SEARCH STUDENT")
    print("4:DELETE STUDENT")
    print("5:EXIT")
    choice = input("ENTER YOUR CHOICE: ")
    if choice == "1":
        name = input("ENTER STUDENT NAME: ")
        students.append(name)
        print("STUDENT ADDED SUCCESSFULLY!")
    elif choice == "2":
        if len(students) == 0:
            print("STUDENT NOT FOUNT")
        else:
            print("\nstudent list: ")
            for student in students:
                print(student)
    elif choice == "3":
        name = input("SEARCH STUDENT HERE!!!!: ")
        if name in students:
            print("STUDENT FOUND!")
        else:
            print("STUDENT NOT FOUND")
    elif choice == "4":
        name = input("ENTER STUDENT NAME TO DELETE :   ")
        if name in students:
            students.remove(name)
            print("DELETE SUCCESSFULY")
        else:
            print("SUDENT CAN'T TO BE FOUND")
    elif choice == "5":
        print("program exited")
        break
    else:
        print("YOUR CHOICE IS OUT OF LIST\nPLEASE CHANGE THE CHOICE ")