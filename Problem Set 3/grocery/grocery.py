dic = {}

while True:
    try:
        item = input().upper()

        if item not in dic:
            count = 1
            dic[item] = count

        else:
            count += 1
            dic[item] = count

    except EOFError:
        for item in sorted(dic):
            print(dic[item], item)
        break