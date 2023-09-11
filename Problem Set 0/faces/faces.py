def convert_face(mood):
    mood = mood.replace(":)", "🙂").replace(":(", "🙁")
    return mood

def main():
    user_input = input()
    print(convert_face(user_input))

main()