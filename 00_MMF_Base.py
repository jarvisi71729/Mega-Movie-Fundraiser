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

# * * * * * Main routine * * * * *

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary

# Loop to get ticket details

# start of loop

# initialise loop so that it runs at least once

name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats are left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    else:
        print("*** You have one seat left ***")

    # Get details...

    # Get name (can't be blank)
    name = not_blank("What's your name? ")
    print()

    if name == "xxx":
        print("You have sold {} tickets. \n"
              "There are {} places still available".format(count, MAX_TICKETS - count))

    count += 1

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")



    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)


# Caculate Total sales and profit

# Output data to text file