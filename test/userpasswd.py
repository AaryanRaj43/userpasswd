new = input("are you creating a new user? y/n ")
new = new.lower()


usr = []
pd = []

if new == "y":
    username = input("Enter a username: ")
    passw = input("Enter a password: ")
    usr.append(username)
    pd.append(passw)
    resp = input("would you like to login y/n: ")
    resp = resp.lower()

    if resp == "y":
        user = input("Enter your username: ")
        password = input("Enter your password: ")
    else:
        print

    x = usr.index(username)
    y = pd.index(passw)

else:
   

    user = input("Enter your username: ")
    password = input("Enter your password: ")

    usr.append(user)
    pd.append(password)


    x = usr.index(user)
    y = pd.index(password)








if x == y:

    print("sucessful")






