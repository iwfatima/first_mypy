def get_input(prompt, required=True, numeric=False):
    while True:
        value = input(prompt)
        if required and not value.strip():
            print("This field is required. Please enter a value.")
            continue
        if numeric:
            if not value.isdigit():
                print("Please enter a valid number.")
                continue
        return value

Name = get_input("What is your first name? ")
Family = get_input("What is your last name? ")
Age = get_input("How old are you? ", numeric=True)
Color = get_input("What is your favorite color? ")
Food = get_input("What is your favorite food? ")
Exercise = get_input("What is your favorite sport? ")
Birthday = get_input("When is your birthday? ")
Book = get_input("What is your favorite book? ")
Purpose = get_input("What is your goal? ")
The_animal = get_input("What is your favorite animal? ")

print("\n--- Your Personal Story ---\n")
print(f"Hi, my name is {Name} {Family}.")
print(f"I am {Age} years old.")
print(f"My favorite color is {Color} and I love eating {Food}.")
print(f"I enjoy playing or watching {Exercise} in my free time.")
print(f"I was born on {Birthday}.")
print(f"One of my favorite books is '{Book}'.")
print(f"I really like {The_animal}s.")
print(f"My current goal is: {Purpose}.")