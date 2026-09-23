








username = input("Enter your username:")
password = input("Enter your password:")
if username=="Hanna":
    if password=="1234":
        print("LOGIN SUCCESSFUL!")
        phone = input("Enter your phone number:")
        code = input("Enter verification code:")
        print("WELCOME TO YOUR ACCOUNT!")
    else:
        print("INCORRECT PASSWORD!")
else:
    if password=="1234":
        print("INCORRECT USERNAME!")
    else:
        print("INCORRECT USERNAME & PASSWORD!")