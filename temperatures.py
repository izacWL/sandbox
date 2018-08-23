
def main():
    temperature = int(input("Please enter a temperature to convert"))
    print(" is the temperature in (C)elsius or (F)ahrenheit  ")
    temp_choice = input()

    if temp_choice == "C":
        return celsius(temperature)
    else:
        return fahrenheit(temperature)


def celsius(temperature):
    celsius_convert = (temperature * 1.8) + 32
    print(celsius_convert)

def fahrenheit(temperature):
    fahrenheit_concert = (temperature - 32) * 0.5556
    print(fahrenheit_concert)
main()
