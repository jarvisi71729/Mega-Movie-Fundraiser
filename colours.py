# # print (u"\u001b[31mHello World")
#

print(u"\u001b[30m Black = 30 "
      u"\u001b[31m Red = 31 \u001b[32m Green = 32 \u001b[33m Gold/Yellow = 33 \u001b[0m")
print(u"\u001b[34m Dark Blue = 34 \u001b[35m Pink = 35 \u001b[36m Light Blue = 36 \u001b[37m Grey = 37 \u001b[0m")


black = u"\u001b[30m"
red = u"\u001b[31m"
green = u"\u001b[32m"
gold = u"\u001b[33m"
end = u"\u001b[0m"
dblue = u"\u001b[34m"
pink = u"\u001b[35m"
lblue = u"\u001b[36m"
grey = u"\u001b[37m"
xxx = u"\u001b[37m\u001b[0m\u001b[36m"


print("{}sausage".format(dblue))
print("{}john".format(xxx))
print()
print("{}Merry {}Chri{}stmas{}".format(red, green, red, end))
print("Hello")


#
#
# red = "\033[31m"
# reset = "\033[0m"
# print("i am {} red {} sausage".format(red, reset))
# orange = "\033[37m"
# print("this is a nice{} orange colour{}, unlike this plain {}red, uwu".format(orange, reset, red))
# black = "\e[0;30m"
# green = "\e[0;32m"
# cyan = \e[0;36m]
#
# print("{}cyan, {}green, {}black".format(cyan, green, black))
#
#
# Blue             \e[0;34m
# Green            \e[0;32m
# Cyan             \e[0;36m
# Red              \e[0;31m
# Purple           \e[0;35m
# Brown            \e[0;33m
# Gray             \e[0;37m
# Dark Gray        \e[1;30m
# Light Blue       \e[1;34m
# Light Green      \e[1;32m
# Light Cyan       \e[1;36m
# Light Red        \e[1;31m
# Light Purple     \e[1;35m
# Yellow           \e[1;33m
# White            \e[1;37m

# import random

# black = u"\u001b[30m, ]"
# red = u"\u001b[31m, ]"
# green = u"\u001b[32m, ]"
# gold = u"\u001b[33m, ]"
# blue = u"\u001b[34m, ]"
# pink = u"\u001b[35m, ]"
# light_blue = u"\u001b[36m, ]"
# grey = u"\u001b[37m, ]"

# black = "\e[0;30m"
# green = "\e[0;32m"
# dblue = u"\u001b[34m"


# colours = ('black', 'red', 'green', 'gold', 'blue', 'pink', 'light_blue', 'grey')
# colours = ("black", "red", "green", "gold", "blue", "pink", "light_blue", "grey")
colours = ("black", "green", "cyan")

colour = random.choice(colours)


