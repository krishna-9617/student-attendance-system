attendance = {}
def markattendance():
  while True:
    print("\n==ATTENDANCE MARKING==")
    name = input("enter the name of student [enter EXIT to exit]: ")
    name = name.lower()
    if(name=="exit"):
        break
    else:
        status = input("absent or present (a/p): ")
        status = status.lower()
        if(status == "p"):
            attendance[name]= "present"
        elif(status == "a"):
            attendance[name] = "absent"
        else:
            print("invalid input")

def viewattendance():
    print("\n==VIEW ATTENDANCE==")
    if len(attendance)==0:
        print("no data available")
        return
    else:
        for i in attendance:
            print(i,":",attendance[i])

def attendance_analysis():
  print("\n==ATTENDANCE ANALYSIS==")
  if len(attendance)==0:
    print("no data available")
    return 

  else:
    keys = list(attendance.values())
    present = keys.count("present")
    total = len(attendance)
    absent = total - present
    present_per = (present/total)*100
    print("total students: ",total)
    print("present students: ",present)
    print("absent students: ",absent)
    print("present percentage: ",present_per,"%")

def clearattendance():
    print("\n==CLEAR ATTENDANCE==")
    confirm = input("are you sure to clear all data? (yes/no): ")
    if confirm == "yes":
        attendance.clear()
        print("all data cleared")
    else:
        print("cancelled")
def search_student():
    print("\n==SEARCH STUDENT==")
    if len(attendance) == 0:
        print("no data available")
        return
    name = input("enter student name: ")
    name = name.lower()
    if name in attendance:
        print(name, ":", attendance[name])
    else:
        print("student not found")

def edit_attendance():
    print("\n==EDIT ATTENDANCE==")
    if len(attendance) == 0:
        print("no data available")
        return
    name = input("enter student name: ")
    name = name.lower()
    if name in attendance:
        print("current status:", attendance[name])
        status = input("enter new status (a/p): ")
        status = status.lower()
        if status == "p":
            attendance[name] = "present"
            print("updated successfully")
        elif status == "a":
            attendance[name] = "absent"
            print("updated successfully")
        else:
            print("invalid input")
    else:
        print("student not found")

def filter_by_status():
    print("\n==FILTER BY STATUS==")
    if len(attendance) == 0:
        print("no data available")
        return
    choice = input("show (p)resent or (a)bsent?: ")
    choice = choice.lower()
    if choice == "p":
        print("\nPRESENT STUDENTS:")
        for i in attendance:
            if attendance[i] == "present":
                print(i)
    elif choice == "a":
        print("\nABSENT STUDENTS:")
        for i in attendance:
            if attendance[i] == "absent":
                print(i)
    else:
        print("invalid input")

def delete_student():
    print("\n==DELETE STUDENT==")
    if len(attendance) == 0:
        print("no data available")
        return
    name = input("enter student name: ")
    name = name.lower()
    if name in attendance:
        confirm = input("are you sure? (yes/no): ")
        if confirm == "yes":
            del attendance[name]
            print("deleted successfully")
        else:
            print("cancelled")
    else:
        print("student not found")

def count_students():
    print("\n==STUDENT COUNT==")
    total = len(attendance)
    print("total students:", total)
    if total > 0:
        present = 0
        absent = 0
        for i in attendance:
            if attendance[i] == "present":
                present = present + 1
            else:
                absent = absent + 1
        print("present:", present)
        print("absent:", absent)



def main():
    while True:
        print("\n==OPTIONS==")
        print("enter 1 to mark attendance")
        print("enter 2 to view the attendance")
        print("enter 3 to analyse the attendance")
        print("enter 4 to clear record")
        print("enter 5 to search student")
        print("enter 6 to edit attendance")
        print("enter 7 to filter by status")
        print("enter 8 to delete student record")
        print("enter 9 to count students")
        print("enter 10 to exit")
        choice = input("enter the choice between 1-10: ")
        if choice == "1":
            markattendance()
        elif choice == "2":
            viewattendance()
        elif choice == "3":
            attendance_analysis()
        elif choice == "4":
            clearattendance()
        elif choice == "5":
            search_student()
        elif choice == "6":
            edit_attendance()
        elif choice == "7":
            filter_by_status()
        elif choice == "8":
            delete_student()
        elif choice == "9":
            count_students()
        elif choice == "10":
            break
        else:
            print("\ninvalid input")

main()
