class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    disp_cups = 9
    money = 550
    espresso_price = 4
    latte_price = 7
    cappuccino_price = 6
    not_enough = ''

    def stocks(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.disp_cups, 'of disposable cups')
        print(self.money, 'of money')

    def buy(self, drink_water, drink_milk, drink_beans, drink_price):
        self.water -= drink_water
        self.milk -= drink_milk
        self.beans -= drink_beans
        self.disp_cups -= 1
        self.money += drink_price

    def check_stocks(self, drink):
        if drink == 1:
            if self.water >= 250:
                if self.beans >= 16:
                    return True
                else:
                    print('Sorry, not enough beans!')
            else:
                print('Sorry, not enough water!')
        elif drink == 2:
            if self.water >= 350:
                if self.milk >= 75:
                    if self.beans >= 16:
                        return True
                    else:
                        print('Sorry, not enough beans!')
                else:
                    print('Sorry, not enough milk!')
            else:
                print('Sorry, not enough water!')
        elif drink == 3:
            if self.water >= 200:
                if self.milk >= 100:
                    if self.beans >= 12:
                        return True
                    else:
                        print('Sorry, not enough beans!')
                else:
                    print('Sorry, not enough milk!')
            else:
                print('Sorry, not enough water!')


coffee = CoffeeMachine()
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        drink = input()
        if drink == '1':
            if coffee.check_stocks(1) and coffee.not_enough == '':
                coffee.buy(250, 0, 16, 4)
                print('I have enough resources, making you a coffee!')
            continue
        elif drink == '2':
            if coffee.check_stocks(2) and coffee.not_enough == '':
                coffee.buy(350, 75, 20, 7)
                print('I have enough resources, making you a coffee!')
            continue
        elif drink == '3':
            if coffee.check_stocks(3) and coffee.not_enough == '':
                coffee.buy(200, 100, 12, 6)
                print('I have enough resources, making you a coffee!')
            continue
        elif drink == 'back':
            continue
    elif action == 'fill':
        print('Write how many ml of water do you want to add:')
        add_water = int(input())
        coffee.water += add_water
        print('Write how many ml of milk do you want to add:')
        add_milk = int(input())
        coffee.milk += add_milk
        print('Write how many grams of coffee beans do you want to add:')
        add_beans = int(input())
        coffee.beans += add_beans
        print('Write how many disposable cups of coffee do you want to add:')
        add_disp_cups = int(input())
        coffee.disp_cups += add_disp_cups
        continue
    elif action == 'take':
        print('I gave you $', coffee.money)
        coffee.money = 0
        continue
    elif action == 'remaining':
        coffee.stocks()
        continue
    elif action == 'exit':
        break
