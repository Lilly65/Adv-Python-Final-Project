import Battle
import Characters
import Create

# C:\Users\lilli\VSCode\Coding Temple\PythonLearning\Pythonfinalproject
def main():
    player = Create.create_character()
    wizard = Characters.EvilWizard("The Dark Wizard")
    Battle.battle(player, wizard)

if __name__ == "__main__":
    main()