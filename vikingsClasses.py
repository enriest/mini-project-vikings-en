import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength 
    def attack(self):
        # your code here
        return self.strength
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name = name
        self.health = health
        self.strength = strength
    def battleCry(self):
        # your code here
        return "Odin Owns You All!"
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        # Return a string to match the subclasses' return type
        if self.health >= 1:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    def receiveDamage(self, damage): 
        # your code here
        self.health -= damage
        if self.health >= 1:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        # your code here
            self.vikingArmy = []
            self.saxonArmy = []
    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = viking.strength
        result = saxon.receiveDamage(damage)
        for saxon in self.saxonArmy:
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            else:
                break
        return result
     
    def saxonAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = saxon.strength
        result = viking.receiveDamage(damage)
        for viking in self.vikingArmy:
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            else:
                break
        return result
    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


