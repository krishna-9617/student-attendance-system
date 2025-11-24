attendance = {}
def markattendance():
  while True:
    print("\n==ATTENDANCE MARKING==")
    name = input("enter the name of student (enter EXIT to exit): ")
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
    present_per = (present/total)*100
    print("total students: ",total)
    print("present students: ",present)
    print("present percentage: ",present_per,"%")

def clearattendance():
    print("\n==CLEAR ATTENDANCE==")
    confirm = input("are you sure ? (yes/no): ")
    if confirm == "yes":
        attendance.clear()
        print("cleared")
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
        print("not found")

def edit_attendance():
    print("\n==EDIT ATTENDANCE==")
    if len(attendance) == 0:
        print("no data available")
        return
    name = input("enter student name: ")
    name = name.lower()
    if name in attendance:
        print("name  is",attendance[name])
        status = input("present status (a/p): ")
        status = status.lower()
        if status == "p":
            attendance[name] = "present"
            print("updated")
        elif status == "a":
            attendance[name] = "absent"
            print("updated")
        else:
            print("invalid input")
    else:
        print("no student found")


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
            print("deleted ")
        else:
            print("cancelled")
    else:
        print("no student found")


def main():
    while True:
        print("\n==OPTIONS==")
        print("enter 1 to mark attendance")
        print("enter 2 to view the attendance")
        print("enter 3 to analyse the attendance")
        print("enter 4 to clear record")
        print("enter 5 to search student")
        print("enter 6 to edit attendance")
        print("enter 7 to delete student record")
        print("enter 8 to exit")
        choice = input("enter the choice between 1-8: ")
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
            delete_student()
        elif choice == "8":
            break
        else:
            print("\ninvalid input")

main()
