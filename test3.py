class Category:    

    def __init__(self, name):

        # Initialize name, ledger, total, spendage
        self.name = name 
        self.ledger = list()
        self.total = 0.0
        self.spendage = 0.0
    
    def deposit(self, amount, description = ""):

        # Append deposit dict to ledger
        self.ledger.append({"amount": amount, "description": description})

        # Add deposit to total
        self.total += amount
        
        return

    def withdraw(self, amount, description = ""):

        # Check if amount can be withdrawn
        if self.check_funds(amount):

            # Append withdrawl dict to ledger
            self.ledger.append({"amount": -amount, "description": description})
    
            # Substract withdrawl from total
            self.total -= amount

            # Add withdrawl to spendage
            self.spendage += amount
        
            return True
        
        # If amount cannot be withdrawn
        return False

    def get_balance(self):

        # Return total
        return format(self.total, ".2f")
        
    def transfer(self, amount, category):

        # Check if amount can be withdrawn and withdraw
        if self.withdraw(amount, f"Transfer to {category.name}"):
            
            # Deposit to specified category
            category.deposit(amount, f"Transfer from {self.name}")
    
            return True
    
        # If amount cannot be withdrawn
        return False

    def check_funds(self, amount):

        # Check if amount withdrawn fits total
        if amount <= self.total:
        
            return True
    
        # If amount cannot be withdrawn
        return False
        # Chat GPT condensed this to return amount <= self.total

    def __str__(self):
    
        # Initialize message with formatted category name
        message = self.name.center(30, "*") + "\n"

        # Iterate through each transaction in ledger
        for item in self.ledger:

            # Format descriptions and amounts
            description = str(item["description"])[:23].ljust(23, ' ')
            amount = format(item['amount'], '.2f')[:7].rjust(7, ' ')
            # ChatGPT removed ", ' ' " from the rjust and ljust
            
            # Append formatted descriptions and amounts to message
            message += f"{description}{amount}\n"

        # Append total to end of string
        message += f"Total: {format(self.total, '.2f')}"
                
        return message

def create_spend_chart(categories): # ChatGPT 

    # Initialize message and total
    message = "Percentage spent by category\n"
    total = 0.0
    longest_name = None

    # Initialize graph variables
    y_axis = list()
    data = list()
    names = list()

    # Adjust scale
    upper_bound = 100
    lower_bound = 0
    step = 10

    # Build y-axis scale
    for tick in range(upper_bound, lower_bound-step, -step):

        # Format y-axis scale 
        y_axis.append(f"{str(tick).rjust(3, ' ')}|")

    length_y_axis = len(y_axis)

    # Iterate over categories for total
    for category in categories:

        # Sum total spendage
        total += category.spendage

        # Find length of longest category name
        if longest_name == None or len(category.name) > longest_name:
            longest_name = len(category.name)

    # Iterate over categories for bar value
    for category in categories:

        # Calculate bar value for each category
        bar_value = int(category.spendage/total*upper_bound/step)

        # Format data vertically
        data.append(str('o' * (bar_value + 1)).rjust(length_y_axis, ' '))

        # Format x-axis labels
        names.append(category.name.ljust(longest_name))

    # Format display of spend chart
    for i in range(length_y_axis):
        message += y_axis[i] + " "
        for datum in data:
            message += datum[i] + "  "
        message += "\n"

    message += "    ----------\n"

    # Format display of x-axis labels
    for i in range(longest_name):
        message += "     "
        for name in names:
            message += name[i] + "  "
        message += "\n"

    return message



# Create food category
food = Category("Food")

# Manipulate food category
food.deposit(1000, "initial deposit") 
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())



# Create clothing category
clothing = Category("Clothing")

# Manipulate clothing category
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)



# Create auto category
auto = Category("Auto")

# Manipulate auto category
auto.deposit(1000, "initial deposit")
auto.withdraw(15)



# Display 
print(food)
print(clothing)
print(auto)


print(create_spend_chart([food, clothing, auto]))


business = Category("Business")
entertainment = Category("Entertainment")

business.deposit(1000)
food.deposit(1000)
entertainment.deposit(1000)

food.withdraw(70)
entertainment.withdraw(30)

print(create_spend_chart([business, food, entertainment]))

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(business)
print(food)
print(entertainment)

print(create_spend_chart([business, food, entertainment]))
