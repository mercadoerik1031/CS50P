greeting = input("Gretting: ").lower()

if "hello" in greeting:
    print("$0")

elif greeting.lstrip().startswith("h"):
    print("$20")

else:
    print("$100")