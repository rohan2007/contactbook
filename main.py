import json

while True:
    print("c : Create new contact")
    print("v : View previosly saved contact with a letter for ex -- > ( a )")
    print("s : Specify a name and then view contact similar to that name for ex -- > ( vijay sharma ) ")
    print("q : quit")

    userInput = input(": ").lower()

    if userInput == "c":
        providedName = input("Enter the name: ")
        providedNumber = int(input("Enter the number"))
        firstLetter = providedName[0]

        with open('contact.json', 'w+') as f_obj:
            data = json.load(f_obj)
            if data.has_key(firstLetter):
                data[firstLetter][providedName] = providedNumber
                print("Done")
                continue
            else:
                data[firstLetter] = {}
                data[firstLetter][providedName] = providedNumber
                print("Done")
                continue
    elif userInput == "v":
        providedLetter = input("Enter the letter: ")
        with open('contact.json', 'w+') as f_obj:
            data = json.load(f_obj)
            if data.has_key(providedLetter):
                for key , value in data[providedLetter].items():
                    print(f"Name: {key}, Number: {value}")
                continue
    elif userInput == "s":
        providedName = input("Enter the name: ").lower()
        firstLetter = providedName[0]
        with open('contact.json') as f_obj:
            data = json.load(f_obj)
            if data.has_key(firstLetter):
                if data[firstLetter].has_key(providedName):
                    print(f"Number: {str(data[firstLetter][providedNumber])}")
                    continue
                else:
                    print(f"User {providedName} not found")
                    continue

    elif userInput == "q":
        print("quitting")
        break