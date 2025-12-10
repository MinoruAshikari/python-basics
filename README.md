# python-basics
"Daily Python learning logs: variables, loops, functions, lists, dictionaries, and mini apps."
name = "Minoru"
country = "Japan"
age = 40

print(name)
print(country)
print(age)

print(f"My name is {name} and I live in {country}. I am {age} years old.")

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are underage.")

score = 75

if score >= 90:
    print("Excellent!")
elif score >= 70:
    print("Good!")
else:
    print("Needs improvement.")

fruits = ["apple", "banana", "orange"]

for f in fruits:
    print(f)

for i in range(1, 6):
    print(i)

pairs = ["USD/JPY", "EUR/USD", "GBP/JPY"]

for p in pairs:
    print("My favorite pair is:", p)

numbers = [10, 20, 30, 40]

print("Numbers list:", numbers)

for n in numbers:
    print("Value =", n)

print("----- Dictionary Test -----")

person = {
    "name": "Minoru",
    "country": "Japan",
    "age": 40
}

print("Name:", person["name"])
print("Country:", person["country"])
print("Age:", person["age"])

print("----- YouTube Data -----")

youtube_video = {
    "title": "My First Python",
    "views": 12000,
    "likes": 850
}

print(youtube_video["title"])
print(youtube_video["views"])
print(youtube_video["likes"])

def greet():
    print("Hello from Python!")

greet()

def greet_user(name):
    print("Hello,", name)

greet_user("Minoru")
greet_user("Alice")

def calc_profit(entry, exit):
    profit = exit - entry
    print("Profit:", profit)

calc_profit(150.25, 150.80)
calc_profit(150.00, 149.50)

def evaluate_views(views):
    if views >= 100000:
        print("Viral!")
    elif views >= 10000:
        print("Good performance")
    else:
        print("Needs improvement")

evaluate_views(120000)
evaluate_views(8000)

# Python Basics by Minoru

This repository contains my learning progress of Python fundamentals.

## ✔ What I learned
- Variables
- Print & f-strings
- If statements
- For loops
- Lists & Dictionaries
- Functions
- Basic mini-tools (FX profit calculator, YouTube evaluation)

## ✔ Purpose
This repo documents my daily progress in Python as I move toward AI, automation, and data-related projects.

## ✔ Files
- `lesson1_variables.py`: Variables and f-strings
- `lesson2_if.py`: Conditional logic
- `lesson3_for.py`: Looping techniques
- `lesson4_list_dict.py`: Lists and dictionaries
- `lesson5_functions.py`: Creating and calling functions



