# CloudOfNiko
# 23.03.2026
# Learning to use default Python modules.

from random import randint

class Die:
    """A model of dice, which you can roll for a random number."""
    def __init__(self, times=1, sides=6):
        """Initialize dice attributes."""
        
        if sides:
            self.sides = sides
        if times:
            self.times = times

    def roll_dice(self):
        """Simulate dice rolls."""

        print(f"\tThis is a {self.sides}-sided die.\n")
        
        for time in range(1, self.times+1):
            number = randint(1, self.sides)
            print(f"Roll №{time} - {number}")

Dice_1 = Die(10)
Dice_2 = Die(10, 10)
Dice_3 = Die(10, 20)
Dice_4 = Die(10)

Dice_1.roll_dice()
print("\n")
Dice_2.roll_dice()
print("\n")
Dice_3.roll_dice()
print("\n")
Dice_4.roll_dice()
