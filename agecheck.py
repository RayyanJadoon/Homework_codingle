age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    print("Age is valid.")
    if age % 2 == 0:
        print("Age is even.")
    else:
        print("Age is odd.")
else:
    print("Invalid age entered.")