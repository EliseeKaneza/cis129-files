# Pet class definition
class Pet:
    def __init__(self, name="", type="", age=0):
        self.__name = name
        self.__type = type
        self.__age = age

    # Setters
    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age

    # Getters
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

# Main program
def main():
    # Create a Pet object
    animal = Pet()

    # Get user input
    inputName = input("Enter a pet name: ")
    animal.setName(inputName)

    inputType = input("Enter a pet type: ")
    animal.setType(inputType)

    inputAge = int(input("Enter a pet age: "))
    animal.setAge(inputAge)

    # Display pet info
    print("The pet name is:", animal.getName())
    print("The pet type is:", animal.getType())
    print("The pet age is:", animal.getAge())

# Run the program
if __name__ == "__main__":
    main()
