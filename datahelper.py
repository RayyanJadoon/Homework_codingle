class DailyDataHelper:

    def __init__(self):
        print("Helper started.")

    def show_message(self):
        message = input("Type a message: ")
        print("Uppercase:", message.upper())

    def find_numbers(self):
        numbers = [2, 4, 6, 8, 10]
        target = int(input("Enter a target number: "))

        found = False

        for i, num1 in enumerate(numbers):
            for j, num2 in enumerate(numbers):
                if i != j and num1 + num2 == target:
                    print("Found:", num1, "+", num2, "=", target)
                    found = True
                    return

        if not found:
            print("No match found.")

    def __del__(self):
        print("Helper closed.")


helper = DailyDataHelper()
helper.show_message()
helper.find_numbers()

del helper