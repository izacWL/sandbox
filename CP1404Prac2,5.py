finished = False
result = 0
while not finished:
    try:
        input("please enter valid number")

        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)