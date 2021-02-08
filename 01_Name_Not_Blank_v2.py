#   Functions go here


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# Main routine goes here

name = not_blank("What's your name? ",
                 "Sorry - this can't be blank, "
                 "please enter your name")