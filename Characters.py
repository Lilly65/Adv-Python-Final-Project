# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.abilitiesInfo = []

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        print(f"{self.abilitiesInfo[0]}")
        print(f"{self.abilitiesInfo[1]}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=180, attack_power=30)
        self.abilityList = [self.berserk, self.shieldWall]
        self.abilities = ["Berserk", "Shield Wall"]
        self.abilitiesInfo = [
            "Berserk: Gain attack power at the cost of health.", 
            "Shield wall: Prevent damage for one turn and take reduced damage for 2 turns after (One time use)."]
        self.berserk = 0
        self.shieldWall = 0
        self.shieldWallCasts = 1

    def berserk(self):
        # Lose 40 hp and gain 10 attack power
        print("You cast Berserk!")
        self.health -= 40
        self.attack_power += 10
        return
    
    def shieldWall(self):
        # Take 0 damage for one turn and 10 less for the following 2 turns
        # One time use
        if self.shieldWallCasts <= 0:
            print("You fail to cast Shield Wall!")
            return
        self.shieldWallCasts = 0
        self.shieldWall = 3
        return

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.abilityList = [self.fireBall, self.iceBarrier]
        self.abilities = ["Fire Ball", "Ice Barrier"]
        self.abilitiesInfo = [
            "Fire Ball: Shoot a ball of fire for 50 damage (2 uses).", 
            "Ice Barrier: Freeze yourself and take no damage for 1 turn."]
        self.fireballCasts = 2
        self.fireball = 0
        self.iceBarrier = 0
    
    def fireBall(self):
        if self.fireballCasts <= 0:
            print("You fail to cast Fire Ball!")
            return
        self.fireball = 1
        print("You cast Fire Ball!")
        self.fireballCasts -= 1
        return
    
    def iceBarrier(self):
        # Take no damage for 2 turns
        # Cannot act
        print("You cast Ice Barrier!")
        self.iceBarrier = 1
        return

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=30)
        self.abilityList = [self.quickShot, self.evasion]
        self.abilities = ["Quick Shot", "Evasion"]
        self.abilitiesInfo = [
            "Quick Shot: Attack twice with inaccurate arrows that do random damage (2 uses).", 
            "Evasion: Take 0 damage from the next attack."]
        self.evasion = 0
        self.quickShotCasts = 3
        self.quickShot = 0
    
    def quickShot(self):
        if self.quickShotCasts <= 0:
            print("You fail to cast Quick Shot!")
            return
        # Attack twice for damage between 20-25
        # Can only be used three times
        print("You cast Quick Shot!")
        self.quickShotCasts -= 1
        self.quickShot = 1
        return
    
    def evasion(self):
        # Take 0 damage from next attack
        print("You cast Evasion!")
        self.evasion = 1
        return

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=25)
        self.abilityList = [self.holyGround, self.sacredBubble]
        self.abilities = ["Holy Ground", "Sacred Bubble"]
        self.abilitiesInfo = [
            "Holy Ground: Consecrate the surrounding ground damage enemies and healing yourself (One time use).", 
            "Sacred Bubble: Channel divine energy to prevent damage for two rounds (One time use)."]
        self.holyGround = 0
        self.holyGroundCasts = 1
        self.sacredBubble = 0
        self.sacredBubbleCasts = 1
    
    def holyGround(self):
        if self.holyGroundCasts <= 0:
            print("You fail to cast Holy Ground!")
            return
        # Regenerate 10 hp every turn for 2 turns
        # Evil wizard takes 5 damage for 2 turns
        # Stops Evil Wizard from healing during its duration
        # One time use
        print("You cast Holy Ground!")
        self.holyGround = 2
        self.holyGroundCasts -= 1
        return
    
    def sacredBubble(self):
        if self.sacredBubbleCasts <= 0:
            print("You fail to cast Sacred Bubble!")
            return
        # Take no damage for 2 turns
        # One time use
        print("You cast Sacred Bubble!")
        self.sacredBubbleCasts = 0
        self.sacredBubble = 2
        return

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=300, attack_power=15)
        self.chargeAttackCount = 0

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def chargeAttack(self):
        if self.chargeAttackCount == 0:
            self.chargeAttackCount = 2
            print("The Dark Wizard prepares his ultimate attack!")
        elif self.chargeAttackCount == 2:
            self.chargeAttackCount = 1
            print("The Dark Wizard is about to unleash his attack!")
        elif self.chargeAttackCount == 1:
            self.chargeAttackCount = -1
            print("The Dark Wizard unleashes his spell!")
        # Show message "Evil wizard prepares his ultimate attack"
        # Next turn "Evil wizard is about to unleash his attack"
        # Next turn do 9999 damage
        return