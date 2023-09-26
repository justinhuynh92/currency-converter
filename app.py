#create function that converts the currency
def main():
    print("This program converts US dollars to Pounds Sterling")
    print()
    #create variable that evaluates the input
    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "pounds.")

#create variable that converts USD to current pounds
#pass the dollars argument to lambda, which will take the expression given and pass it to the variable
convert_to_pounds = lambda dollars: dollars * 0.82

main()
