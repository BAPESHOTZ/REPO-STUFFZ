#authentication program

def authentication(input1,input2):
    if input1 == 'jackripper':
        if input2 == 'password':
            print("user has been authenticated")
        else:
            print("wrong password")
    else:
        print("wrong user")

#login

username = str(input("enter username here: "))
password = str(input("enter password here: "))

authentication(username,password)


