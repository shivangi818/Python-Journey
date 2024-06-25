email= input("Enter your email")


if "@" in email:
    #paste
 Password= input("enter your password")
 if email=="xyz123@gmail.com" and Password=="1234":
    print("welcome")
 elif email == "xyz123@gmail.com" and Password!="1234":
    print("wrong Password")
    Password=input("enter your password again")
    if Password=="1234":
        print("welcome finally")
    else:
        print("sorry wrong Password again")
    
    
 else:
    print("Incorrect")




else:
    print("not a valid email")
