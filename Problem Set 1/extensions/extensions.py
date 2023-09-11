file_name = input("File name: ").strip().lower()
if "." not in file_name:
    print("application/octet-stream")
    exit()

extension = file_name.split(".")[-1]

match extension:
    case "gif" | "jpeg" | "png":
        print(f"image/{extension}")

    # this is need to get 100% using check50
    # when .jpg is input expected output is .jpeg
    case "jpg":
        print(f"image/jpeg")

    case "pdf" | "zip":
        print(f"application/{extension}")

    case "txt":
        print(f"text/plain")

    case _:
        print("application/octet-stream")