class Enemy:
    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def can_cast(self):
        pass

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.is_alive is False:
            return False
        if self.health + healing_points > 100:
            self.health = 100
        else:
            self.health = self.health + healing_points
        return True

    def take_mana(self, mana_points):
        pass
