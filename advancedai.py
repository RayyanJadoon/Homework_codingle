name = input("What is your name? ")
print("Hello", name)

while True:
    mood = input("How are you? (good, bad, neutral): ")

    if mood == "good":
        print("That's great!")
    elif mood == "bad":
        print("Sorry to hear that.")
    else:
        print("Okay!")

    hobby = input("What is your favourite hobby? ")
    print("Cool!")

    again = input("Do you want to continue? (yes/no): ")

    if again == "no":
        print("Goodbye", name)
        break