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
def greet_user(name):
    print("Hello,", name)

greet_user("Minoru")
greet_user("Alice")

