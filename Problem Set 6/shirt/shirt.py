import sys
import os


from PIL import Image, ImageOps


def main():
    if is_valid_argv(sys.argv):
        paste_shirt(sys.argv[1], sys.argv[2])


def paste_shirt(before, after):
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(before) as base_layer:
                base_layer = ImageOps.fit(base_layer, shirt.size)
                base_layer.paste(shirt, shirt)
                base_layer.save(after)

    except FileNotFoundError:
        sys.exit("Input does not exist")


def is_valid_argv(argv):
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")

    before = os.path.splitext(argv[1])
    after = os.path.splitext(argv[2])

    extentions = [".png", ".jpg"]

    if before[1].lower() not in extentions:
        sys.exit("Invalid Input")

    if before[1].lower() != after[1].lower():
        sys.exit("Input and output have different extensions")

    return True


if __name__ == "__main__":
    main()
