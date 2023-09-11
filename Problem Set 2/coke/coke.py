# amount_due = 50
# quarter = 25
# dime = 10
# nickle = 5

# while True:
#     print(f"Amount Due: {amount_due}")

#     inserted_coin = int(input("Insert Coin: "))

#     if inserted_coin == quarter or inserted_coin == dime or inserted_coin == nickle:
#         amount_due -= inserted_coin

#         if amount_due <= 0:
#             print(f"Change Owed: {abs(amount_due)}")
#             break

#     else:
#         continue

amount_due = 50
valid_coins = (25, 10, 5)

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    inserted_coin = int(input("Inserted Coin: "))

    if inserted_coin in valid_coins:
        amount_due -= inserted_coin

    else:
        continue

print(f"Change Owed: {abs(amount_due)}")