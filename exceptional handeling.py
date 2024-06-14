
# try:
#     num = int(input("Enter the num"))
#     print(num)
# except:
#     print("Try again after solving error")

# print("With the flow")
def fun():
    c=1
    d=5
    try:    
        a=int(input("Enter the number"))
        b = int(input("Enter the 2nd number"))

        if a!=c:
           raise ValueError
           
        elif b!=d:
           raise ZeroDivisionError
        
    except ValueError:  
          print("value is invalid")
          fun()

    except ZeroDivisionError:   
        print("value2 is invalid")
        fun()
    else:
       print("Logeedin")
    finally:
       print("Done")



fun()