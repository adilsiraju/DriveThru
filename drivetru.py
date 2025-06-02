def get_item(x):
    menu = {
        1: "🍔 Cheeseburger",
        2: "🍟 Fries",
        3: "🥤 Soda",
        4: "🍦 Ice Cream",
        5: "🍪 Cookie"
    }
    return menu.get(x, "Sorry, that's not on the menu!")

def welcome():
    print("Hello!\nWelcome to McD!\nToday's Menu:")

def menu():
    print('''
    1. 🍔 Cheeseburger
    2. 🍟 Fries
    3. 🥤 Soda
    4. 🍦 Ice Cream
    5. 🍪 Cookie
    ''')

welcome()
menu()
try:
    option = int(input("What would you like to order? Enter a number (1-5): "))
    print(get_item(option))
    print("You'll recive your order in the next counter.\nThank you for shopping with us.")
except ValueError:
    print("Please enter a valid number.")