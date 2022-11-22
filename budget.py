class Category:
    def __init__(self, name):
        """Class initialization: Assigns each category object:
        * a name
        * an empty ledger
        * an empty balance list
        """
        self.name = name
        self.ledger = list()
        self.balance = list()

    def __str__(self):
        """Definition of the string representation of the objects in the `Category` class."""
        budget_string = f"{self.name:*^30}\n"
        for item in self.ledger:
            budget_string += f"{item['description'][0:23]:23}{item['amount']:>7.2f}\n"
        budget_string += f"Total: " + str(self.get_balance())
        return budget_string

    def check_funds(self, amount):
        """This accepts an amount and returns `True` if the amount can be afforded.
        """
        if amount > self.get_balance():
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        """
        *This method accepts an amount and description.
        *It appends an object to the ledger in the format of `{"amount": amount, "description": description}`.
          """
        self.ledger.append({"amount": amount, "description": description})
        self.balance.append(float(amount))

    def withdraw(self, amount, description=""):
        """
        *This method accepts a negative amount and a description.
        *It appends an object to the ledger in the format of `{"amount": amount, "description": description}`.
        *If there are not enough funds, nothing is added to the ledger and returns False.
        """
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance.append(float(-amount))
            return True
        else:
            return False

    def get_balance(self):
        """
        *This method returns the current balance of the budget category
        """
        return sum(self.balance)

    def transfer(self, amount, category):
        """
        *This method accepts an amount and another budget category
        *It does a withdrawal of the amount from the other budget catagory with a description "Transfer to [Destination Budget Category]". 
        *It then does a deposit of the amount with the description "Transfer from [Source Budget Category]". 
        *If there are not enough funds, nothing is added to either ledgers and returns False
        """
        if self.check_funds(amount) is True:
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

          
#This function accepts the categories listwaa and returns a string bar chart. The chart shows the percentage spent in each category passed in to the function as a fraction of all the withdrawals made."""
def create_spend_chart(categories):

  #this is the heading
    chart = "Percentage spent by category\n"
    percent_list = list()
    balance_spent = 0

    # Calculate balance amount of money spent.
    for category in categories:
        withdraw_amount = -(category.ledger[1]["amount"])
        balance_spent += withdraw_amount

    # Calculate the percentage of money spent for each transaction.
    for category in categories:
        withdraw_amount = -(category.ledger[1]["amount"])
        percent_list.append(int((withdraw_amount / balance_spent) * 100))

    # this adds the graph ticks.
    top = 100
    while top >= 0:
        i = 0
        if len(str(top)) < 3:
            while i < (3 - len(str(top))):
                chart += " "
                i += 1
        chart = chart + str(top) + "|"
      # this adds the data bars
        i = 0
        while i < len(categories):
            if percent_list[i] >= top:
                chart += " o "
            else:
                chart += "   "
            i += 1
        #next row
        chart += " \n"
        top -= 10

    # Create the x axis line.
    chart = chart + "    " + ("---" * len(categories)) + "-"

  # find the longest catagory name
    max_length = 0
    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)

    # Write the category names vertically.      
    i = 0
    while i < max_length:
      #next row
        chart += "\n    "
        for category in categories:
            try:
                chart = chart + " " + category.name[i] + " "
            except:
                chart += "   "
        chart += " "
        i += 1
    return chart