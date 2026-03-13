import Characters
import random

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print(f"2. Use {player.abilities[0]}")
        print(f"3. Use {player.abilities[1]}")
        print("4. View Stats and Ability Info")
        
        if isinstance(player, Characters.Mage):
            if player.fireball == 1:
                print("You cast Fireball!")
                print("The Dark Wizard takes 90 damage!")
                wizard.health -= 90
                player.fireball = 0
                pass
            
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.abilityList[0]()
        elif choice == '3':
            player.abilityList[1]()
        elif choice == '4':
            player.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            hg = getattr(player, "holyGround", False)
            if hg and hg >= 1:
                print("The Dark Wizard's regeneration is prevented by holy ground!")
                print(f"The Dark Wizards current health is: {wizard.health}")
            else:
                wizard.regenerate()
            if wizard.health <= 100 and wizard.health > 0 and wizard.chargeAttackCount != -1:
                wizard.chargeAttack()
            elif wizard.chargeAttackCount >= 1:
                wizard.chargeAttack()
        else:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")
            break

        if isinstance(player, Characters.Warrior):
            if wizard.chargeAttackCount == -1 and player.shieldWall != 3:
                print("The wizard hits you with his ultimate attack dealing 9999 damage!")
                player.health -= 9999
            elif wizard.chargeAttackCount == -1:
                wizard.chargeAttackCount = -2

            if player.shieldWall == 3:
                #Prevent damage
                print("You block the attack with Shield Wall!")
                player.shieldWall -= 1

            elif player.shieldWall >= 1:
                #Reduce damage
                print("You take reduced damage from Shield Wall!")
                print(f"The Dark Wizard attacks {player.name} for 5 damage!")
                player.shieldWall -= 1
                player.health -= 5

            elif wizard.health > 0:
                wizard.attack(player)

        elif isinstance(player, Characters.Mage):
            if wizard.chargeAttackCount == -1 and player.iceBarrier == 0:
                print("The Dark Wizard hits you with his ultimate attack dealing 9999 damage!")
                player.health -= 9999
            elif wizard.chargeAttackCount == -1:
                wizard.chargeAttackCount = -2

            if player.fireball == 1:
                print("The Dark Wizard takes 50 damage!")
                player.fireball = 0
                wizard.health -= 50
            
            if player.iceBarrier == 1:
                print("You block the damage with Ice Barrier!")
                player.iceBarrier = 0

            elif wizard.health > 0 and wizard.chargeAttackCount <= 0:
                wizard.attack(player)


        elif isinstance(player, Characters.Archer):
            if wizard.chargeAttackCount == -1 and player.evasion == 0:
                print("The wizard hits you with his ultimate attack dealing 9999 damage!")
                player.health -= 9999
            elif wizard.chargeAttackCount == -1:
                wizard.chargeAttackCount = -2

            if player.quickShot == 1:
                damage1 = random.randint(20, 25)
                print(f"The Dark Wizard takes {damage1} damage!")
                damage2 = random.randint(20, 25)
                print(f"The Dark Wizard takes {damage2} damage!")
                player.quickShot = 0
                wizard.health -= damage1 + damage2

            if player.evasion == 1:
                print("You evade the attack!")
                player.evasion = 0

            elif wizard.health > 0:
                wizard.attack(player)
            

        elif isinstance(player, Characters.Paladin):
            if wizard.chargeAttackCount == -1 and player.sacredBubble == 0:
                print("The wizard hits you with his ultimate attack dealing 9999 damage!")
                player.health -= 9999
            elif wizard.chargeAttackCount == -1:
                wizard.chargeAttackCount = -2

            if player.holyGround >= 1:
                print("The Dark Wizard is harmed by Holy Ground!")
                if player.health + 10 > player.max_health:
                    print("You fail to heal yourself! (Already max HP)")
                else:
                    print("You are healed by Holy Ground!")
                    player.health += 10
                wizard.health -= 5
                player.holyGround -= 1
            
            if player.sacredBubble >= 1:
                print("You block the damage with Sacred Bubble!")
                player.sacredBubble -= 1

            elif wizard.health > 0:
                wizard.attack(player)
        
        if player.health <= -5000:
            print(f"{player.name} has been erased from existence...")
        elif player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
