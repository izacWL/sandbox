MIN_LENGTH = 10
MAX_LENGTH = 15
def main():
    print("please enter a valid password")
    print ("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, " characters.")
    password = input(">")
    while not is_valid_password(password):
        print("invalid password")
        password = input(">")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))
def is_valid_password(password):
    count_lower = 0
    count_upper = 0
    