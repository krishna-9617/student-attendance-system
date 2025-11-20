attendance = {}
def markattendance():
  while True:
    print("\n==ATTENDACE MARKING==")
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
    print("\n==VIEW ATTENDANCE=='")
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
    print(f"percentage present: {present_per:.2f}%")



def main():
    while True:
        print("\n==OPTIONS==")
        print("enter 1 to mark attendance")
        print("enter 2 to view the attendance")
        print("enter 3 to analyse the attendance")
        print("enter 4 to exit")
        choice = input("enter the choice between 1-4: ")
        if choice == "1":
            markattendance()
        elif choice == "2":
            viewattendance()
        elif choice == "3":
            attendance_analysis()
        elif choice== "4":
          print("Thanks for using Student-Attendance-System")
            break

        else:
            print("\ninvalid input")
main()
