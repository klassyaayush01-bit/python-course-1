while True:
    user_input = input("Enter a number or type 'done': ")

    if user_input.lower() == "done":
        break

    try:
        number = int(user_input)
        print("You entered:", number)
    except ValueError:
        print("Invalid input. Please enter a number.")
