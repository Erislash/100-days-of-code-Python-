from menu import MENU, resources


# TODO: 0. Prompt user by asking “What would you like? (espresso/latte/cappuccino)"     DONE
# TODO: 1. Turn off the Coffee Machine by entering “off” to the prompt.     DONE
# TODO: 2. Print report.        DONE
# TODO: 3. Check resources sufficient?      DONE
# TODO: 4. Process coins.       DONE
# TODO: 5. Check transaction successful?        DONE
# TODO: 6. Make Coffee      DONE


def printReport() -> None:
    print('===========================')
    print('Report ☕:')
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print('===========================')


def checkResources(option: str) -> bool:
    ingredients = MENU[option]['ingredients']
    for ingredient in ingredients.keys():
        if ingredients[ingredient] > resources[ingredient]:
            print(f'Sorry, there\'s not enough {ingredient}')
            return False
    return True


def processCoins(option: str) -> bool:
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    totalMoney = 0

    print('Enter your coins:')

    try:
        quarters = int(input("How many quarters? ")) * 0.25
    except ValueError:
        quarters = 0

    try:
        dimes = int(input("How many dimes? ")) * 0.1
    except ValueError:
        dimes = 0

    try:
        nickles = int(input("How many nickles? ")) * 0.05
    except ValueError:
        nickles = 0

    try:
        pennies = int(input("How many pennies? ")) * 0.01
    except ValueError:
        pennies = 0

    totalMoney = quarters + dimes + nickles + pennies
    print(f"Total money: {totalMoney}")
    if MENU[option]['cost'] > totalMoney:
        print('Not enough money. Money refunded.')
        return False

    print("Here is ${:.2f} dollars in change.".format(totalMoney-MENU[option]['cost']))
    return True


def updateResources(option: str) -> None:
    ingredientsUsed = MENU[option]['ingredients']
    for ingredient in ingredientsUsed:
        resources[ingredient] -= MENU[option]['ingredients'][ingredient]


def processOrder(option: str):
    if not checkResources(option):
        return
    if not processCoins(option):
        return
    updateResources(option)


if __name__ == '__main__':
    option = ''
    while option != 'off':

        print('What would you like?')
        print(f'Espresso - ${MENU["espresso"]["cost"]}')
        print(f'Latte - ${MENU["latte"]["cost"]}')
        print(f'Cappuccino - ${MENU["cappuccino"]["cost"]}')
        option = input('--> ')

        if option == 'espresso' or option == 'latte' or option == 'cappuccino':
            processOrder(option)
        elif option == 'off':
            print('Goodbye!')
        elif option == 'report':
            printReport()
        else:
            print('Unknown command')
