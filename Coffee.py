class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.option = None
        self.run()

    def status(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self):
        self.option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if self.option == "back":
            pass
        elif self.option == "1":
            water_need = self.water - 250
            beans_need = self.beans - 16
            cups_need = self.cups - 1
            bottleneck = min(water_need, beans_need, cups_need)
            if (water_need >= 0) and (beans_need >= 0) and (cups_need >= 0):
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                if bottleneck == water_need:
                    missing = "water"
                elif bottleneck == beans_need:
                    missing = "coffee beans"
                else:
                    missing = "disposable cups"
                print(f"Sorry, not enough {missing}!")
        elif self.option == "2":
            water_need = self.water - 350
            milk_need = self.milk - 75
            beans_need = self.beans - 20
            cups_need = self.cups - 1
            bottleneck = min(water_need, milk_need, beans_need, cups_need)
            if (water_need >= 0) and (milk_need >= 0) and (beans_need >= 0) and (cups_need >= 0):
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                if bottleneck == water_need:
                    missing = "water"
                elif bottleneck == beans_need:
                    missing = "coffee beans"
                elif bottleneck == milk_need:
                    missing = "milk"
                else:
                    missing = "disposable cups"
                print(f"Sorry, not enough {missing}!")
        elif self.option == "3":
            water_need = self.water - 200
            milk_need = self.milk - 100
            beans_need = self.beans - 12
            cups_need = self.cups - 1
            bottleneck = min(water_need, milk_need, beans_need, cups_need)
            if (water_need >= 0) and (milk_need >= 0) and (beans_need >= 0) and (cups_need >= 0):
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                if bottleneck == water_need:
                    missing = "water"
                elif bottleneck == beans_need:
                    missing = "coffee beans"
                elif bottleneck == milk_need:
                    missing = "milk"
                else:
                    missing = "disposable cups"
                print(f"Sorry, not enough {missing}!")
        else:
            pass

    def fill(self):
        self.water = self.water + int(input("Write how many ml of water do you want to add: "))
        self.milk = self.milk + int(input("Write how many ml of milk do you want to add: "))
        self.beans = self.beans + int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups = self.cups + int(input("Write how many disposable cups of coffee do you want to add: "))
                
    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def run(self):
    	counter = 0
    	while counter != 1:
        	action = input("Write action (buy, fill, take, remaining, exit): ")
        	if action == "buy":
        	    self.buy()
        	elif action == "fill":
        	    self.fill()
        	elif action == "take":
        	    self.take()
        	elif action == "remaining":
        	    self.status()
        	else:
        	    break

coffee_maker = CoffeeMachine()
