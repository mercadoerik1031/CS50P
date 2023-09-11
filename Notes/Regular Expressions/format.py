import re


name = input("What's your name? ").strip()

    # match from start any char 1 or more times space any char 1 or more times at end
matches = re.search(r"^.+, .+$", name)

    # () will return what is captured
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")