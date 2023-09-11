import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    user_input = input("Input: ")
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(user_input))

elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and sys.argv[2] in figlet.getFonts()
):
    user_input = input("Input: ")
    font = figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(user_input))

else:
    sys.exit("Invalid usage")
