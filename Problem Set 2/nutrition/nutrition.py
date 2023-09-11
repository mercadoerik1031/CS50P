nutrition_facts = [{"apple": "130"},
                   {"avocado":"50"},
                   {"banana": "110"},
                   {"cantaloupe": "50"},
                   {"grapes": "90"},
                   {"honeydew melon": "50"},
                   {"kiwifruit": "90"},
                   {"lemon": "15"},
                   {"lime": "20"},
                   {"lime": "20"},
                   {"nectarine": "60"},
                   {"orange": "80"},
                   {"peach": "60"},
                   {"pear": "100"},
                   {"pineapple": "50"},
                   {"plums": "70"},
                   {"strawberries": "50"},
                   {"sweet cherries": "100"},
                   {"tangerine": "50"},
                   {"watermelon": "80"},]

user_input = input("Item: ").lower()

for dic in nutrition_facts:
    if user_input in dic:
        print("Calories:", dic[user_input])
        break