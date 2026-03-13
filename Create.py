import Characters

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Characters.Warrior(name)
    elif class_choice == '2':
        return Characters.Mage(name)
    elif class_choice == '3':
        return Characters.Archer(name)
    elif class_choice == '4':
        return Characters.Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Characters.Warrior(name)