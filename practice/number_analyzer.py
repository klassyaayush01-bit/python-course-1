largest = None
smallest = None

while True:
    user_input = input("Enter a number or type 'done' to finish: ")

    if user_input.lower() == "done":
        break

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if largest is None or number > largest:
        largest = number

    if smallest is None or number < smallest:
        smallest = number

if largest is not None:
    print("Largest number:", largest)
    print("Smallest number:", smallest)
else:
    print("No numbers were entered.")
