This is my submission for the final project in the Advanced Python module.

A description of requirement fullilment:
- Added two new classes the archer and the paladin.
- Implemented 2 special abilities for every class:
  - Warrior: Berserk and Shieldwall
  - Mage: Fire Ball and Ice Block
  - Archer: Quick Shot and Evade
  - Paladin: Holy Ground and Sacred Bubble
- Healing mechanic: The paladin's special ability Holy Ground lasts for 3 turns and heals the paladin each turn it is active. If it would heal the paladin over max hp it give a message "Cannot heal over max HP!" and does not heal past max hp.
- Randomize attack damage: The archer's special ability Quick Shot does a random amount of damage between 20-25 as you are shooting two "less accurate" shots.
- Turn based combat: The player fights the evil wizard in a turn based combat with the option to attack, use special abilties, or check status which displays descriptions of the special abilities as well as the players current health.
- Evil Wizard logic: The evil wizard attacks the player each turn and regenerates 5 hp. The paladin's Holy Ground disables the wizard's regeneration while it is active.
- Display victory/defeat messages: The game will display a message in the event of winning or losing. There is a special message that is displayed if the player is defeated by the wizard's Charge Attack
- Bonus task: When the wizard reaches a certain HP threshold the game displays a warning that the wizard is preparing a powerful attack. If the player does not use a defensive ability to block the powerful attack they will take 9999 damage and recieve a special defeat message.
