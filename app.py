#create function that converts the currency
def main():
    print("This program converts US dollars to Pounds Sterling")
    print()
    #create variable that evaluates the input
    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is," pounds, "pounds.")
