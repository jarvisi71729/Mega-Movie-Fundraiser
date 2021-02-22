#   import statements


# functions go here


# checks user's name input is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # if name is not blank, program continues
        if response != "":
            return response

        # if name is blank, print error (& reprint question)
        else:
            print("Sorry - this can't be blank")


# checks for an integer between two values
def int_check(question):

            error = "Please enter a whole number that is more than 12 and less than 130"

            valid = False
            while not valid:

                # ask user for number and check it is valid
                try:
                    response = int(input(question))

                    if response <= 0:
                        print(error)
                    else:
                        return response

                # if an integer is not entered, display an error
                except ValueError:
                    print(error)

# * * * * * Main routine * * * * *

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# start of loop

# initialise loop so that it runs at least once

name = ""
ticket_count = 0
MAX_TICKETS = 5

while name != "xxx" and ticket_count < MAX_TICKETS:

    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    else:
        print("*** You have one seat left ***")

    # Get details...

    # Get name (can't be blank)
    name = not_blank("Name? ")
    # ticket_count += 1
    # print()

# End of tickets loop

    if name == "xxx":
        print("You have sold {} tickets. \n"
              "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))
        break

    # ticket_count += 1

    # Get age (between 12 & 130)
    age = int_check("Age: ")

    # check that age is valid (between 12 & 130)
    if age < 12:
        print("Sorry, you are too young to view this movie")
        continue
    elif age > 130:
        print("Sorry, you are too old")
        continue

    ticket_count += 1

if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)


# Caculate Total sales and profit

# Output data to text file