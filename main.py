name = input("Welcome, what is your name? ")
number = int(input("Hi " + name + ". Enter an integer between 1 and 100 inclusive: "))
while not 1 <= number <= 100:
    number = int(input("Please enter a valid integer between 1 and 100: "))
if number % 2 == 1 and number < 60:
    print(name + ", Your number is odd and less than 60.")
elif number % 2 == 0 and 2 <= number <= 24:
    print(name + ", Your number is even and less than 25.")
elif number % 2 == 0 and 26 <= number <= 60:
    print(name + ", Your number is even and between 26 and 60 inclusive.")
elif number % 2 == 0 and number > 60:
    print(name + ", Your number is even and greater than 60.")
elif number % 2 == 1 and number > 60:
    print(name + ", Your number is odd and greater than 60.")

while True:
    another_numb = input("Would you like to enter another number? y/n ")
    if another_numb == "y":
        number = int((input("Ok, " + name + ", please enter another integer between 1 and 100 inclusive: ")))
        while not 1 <= number <= 100:
            number = int(input("Please enter a valid integer between 1 and 100: "))
        if number % 2 == 1 and number < 60:
            print(name + ", Your number is odd and less than 60.")
        elif number % 2 == 0 and 2 <= number <= 24:
            print(name + ", Your number is even and less than 25.")
        elif number % 2 == 0 and 26 <= number <= 60:
            print(name + ", Your number is even and between 26 and 60 inclusive.")
        elif number % 2 == 0 and number > 60:
            print(name + ", Your number is even and greater than 60.")
        elif number % 2 == 1 and number > 60:
            print(name + ", Your number is odd and greater than 60.")
    elif another_numb == "n":
        break
