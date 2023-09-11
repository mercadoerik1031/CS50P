    # we want to say yes or no this email is valid
'''
email = input("What's your email? ").strip()

username, domain = email.split("@")

    # if username: if string not empty return True
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
'''

    # re library: Regular Expressions

'''
parrterns in re

re.search(pattern, string, flags=0)

. any char except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetition
{m} m repetitions (specify m yourself)
{m,n} m-n repetitions
^ matches the start of the string
$ matches the end of a string or just before the newline at the end of the string
[] set of characters
[^] complementing the set
'''
import re

email = input("Whats's your email? ").strip()

    # r is raw string dont interpet "\"
    # ^ match from start of string
    # $ match from end of string
    # + one or more things to the left
    # [^@] any char except "@"
    # \.edu literal .edu
if re.search(r"^[^@]+@[^@]\.edu$", email):
    # erik@ucsc.edu -> Valid
    # erik@ucsc?edu -> Invalid
    print("Valid")
else:
    print("Invalid")

    # allow all letters a-z and captial
    # allow all number 0-9
    # allow _
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

    # \w is a shortcut for [a-zA-Z0-9_]
    # \w any "word char"
    # (com|edu|gov|net|org) allow this list at the end of the string
if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")

'''
        SHORT CUTS
-----------------------------
\d decimal digit
\D not a decimal digit
\s whitespace character
\S not a whitespace character
\w word character .. as well as numbers and underscore
\W not a word character
A|B either A or B
(...) a group
(?:...) non-capturing version
'''

'''
        FLAGS
----------------------------
re.IGNORECASE
re.MULTILINE
re.DOTALL
'''
    # ignore the case with 3rd parameter
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

    # re.match(pattern, string, flags=0)
    # automaticlly starts matching from start of string
    # re.fullmatch(patter, string, flags=0)
    # automatically matches front of string and end of string

