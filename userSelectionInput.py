user1 = input("Enter the user name")
user = user1.replace(" ","")

# is user is doesnot enters empty string
if user !="":
    # check the user is admin redirect accordingly
    if user == "Admin" or user == "Admin1" or user == "Admin2":
        print("Successfully logged in to admin page")
        attendance1 = input("Enter attendance")
        attendance = attendance1.replace(" ","")
        # check attendance
        if attendance == "Full":
            print("Attendance is full")
        elif attendance == "Half":
            print("Attendance is half")
        elif attendance == "Morning":
            print("Attendance is Morning")
        else:
            print("Absent")
    # redirect to normal user
    else:
        print("Login as normal user")
# is user is enters empty string
else:
    print("Please enter the name it should not be empty")
