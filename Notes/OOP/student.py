'''
def main():
    student = get_student()

    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")

    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
'''

    # tuple (x, y)
    # a list that can not be changed

    # list [x, y, z]
    # a list that can be changed

    # dictionary {"name": name, "house": house}
    # "key" : value pairs that can also be changed

    # classes will be like a blueprint
    # object are attribute using the "."
    # methods: functions inside of classes
'''
class  Student:
    # def __init__ allows you to initialize objects
    # raise lets you come with up with your own exceptions
    def __init__(self, name, house, patronus):
        if not name: # same as if name == ""
            raise ValueError("Missing name")

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")

        self.name = name
        self.house = house
        self.patronus = patronus


    # __str__ print your classes
        # name: Harry house: Gryffindor
        # prints(student): Harry from Gryffindor
    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.patronus:
            case "Stag":
                return "s"
            case "Otter":
                return "o"
            case "Jack Russell Terrier":
                return "d"
            case _:
                return "magic wand"
def main():
    student = get_student()
    print(student) # __str__ method
    print("Expecto Patronum")
    print(student.charm()) # charm method


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
'''

'''
###########################################################################################################
    # properties are like attributes but we have more control over
    # @property
    # decorators functions that modify the behavior of other functions
class  Student:
    def __init__(self, name, house):

        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def name(self):
        return self._name

    @property
    def house(self):
        return self._house

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
'''

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod # I can all this method without instantiating a student first
    def get_student(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # creates an object of the current class


def main():
    student = Student.get_student()
    print(student)


if __name__ == "__main__":
    main()