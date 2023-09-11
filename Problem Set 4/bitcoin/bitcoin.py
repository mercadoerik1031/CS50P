import requests
import sys


if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    dollar = float(sys.argv[-1])
except ValueError:
    sys.exit("command-line argument is not a number")

while True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        break
    except requests.RequestException:
        pass

# print(json.dumps(response.json(), indent=2)) print a string of the json file (makes it look nice)

o = response.json()  # convert o into dict
amount = o["bpi"]["USD"]["rate_float"] * dollar
print(f"${amount:,.4f}")
