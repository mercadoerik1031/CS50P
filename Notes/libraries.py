# library code other people have wrote
# python has a random library
# import key word

########################################################

# generate.py
import random

coin = random.choice(["heads", "tails"])
print(coin)

# use from if i want to use specific functions in a model
from random import choice

# random.randint(a, b) inclusive 1 - 10 including 10
num = random.randint(1, 10)
print(num)

ls = [1, 2, 3]
random.shuffle(ls) # takes a list and moves them randomly (think shuffling cards)

cards = ["jack", "queen", "king"]
for card in cards:
    print(card)

########################################################
# statistics library
import statistics

statistics.mean([100, 90]) # find the average

##########################################################
# command-line arguments
import sys
# sys.argv argument vector
print("hello, my name is", sys.agrv[1])
# when running in cli
# python name.py David; will run and print(hello, my name is David)

# better way to do this
import sys
try:
    print("hello my name is,", sys.argv[1])
except IndexError:
    print("Too few arguments")


# another way to do it. This way it give more information
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is, sys.argv[1]")

# if you use " " in cli it reads as 1 index
    # ex: python name.py "Erik Mercado"
    # prints hello, my name is Erik Mercado

# this will quit the program if there is an error
if len(sys.argv) < 2:
    sys.exit(print("Too few arguments"))
elif sys.exit(len(sys.argv) > 2):
    print("Too many arguments")

print("hello, my name is, sys.argv[1]")


# if there are many words in the command line
if len(sys,argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is arg")
# this will print hello, my name is numpy then the list of names

# slices
if len(sys,argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # skip the the first index of the list
    print("hello, my name is arg")


###########################################################################
# packages a 3rd party library (like numpy matplotlib)
# PyPi pypi.org allows you to download and install all the packages

# cowsay is a package on python
# pip allows to install packages

# pip install cowsay (in cli)

# import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1]) # prints a cow saying hello, [name]

############################################################################
# APIs Application Programming Interface
    # 3rd party service we can write code that talk to

# requests
    # allows you to make web requests
    # automate the retrieval of URLs

# pip install request


# this program will use python to get JSON file from itunes API
    # for the first weezer song on itunes

import json
# import requests
import sys


if len(sys.argv) != 2:
    sys.exit()

response = request.get("https://itunes.apple.com/search?entity=song&limit=1&term" + sys.argv[1])

print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])


#######################################################################################
# custom libraries
# sayings.py
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()

#####################################################################################
# saying.py

import sys

# from sayings import hello

if len(sys.agrv) == 2:
    hello(sys.agrv[1])