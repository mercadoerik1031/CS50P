answer = input("What is the Answer to the Great Question of Life, Universe, and Everything? ").strip().lower()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")