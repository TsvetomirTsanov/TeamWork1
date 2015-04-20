from random import random


class Common:

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health != 0

    def can_cast():
        pass

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if self.is_alive is False:
            return False
        if self.health + healing_points > 100:
            self.health = 100
        else:
            self.health = self.health + healing_points
        return True

    def take_mana(self, mana_point):
        if self.mana + mana.points > 100:
            self.mana = 100
        self.mana += mana.points

    def attack(self):
        pass


class Hero(Common):

    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate=2):
        super().__init__(health, mana)
        self.__name = name
        self.__title = title
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__weapon = Weapon("", 0)
        self.__spell = Spell("", 0, 0)

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

    def equip(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapon = weapon
            print(self.__weapon.name)

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.__spell = spell
            print(self.__spell.name)


class Enemy(Common):

    def __init__(self, health=100, mana=100, damage=20):
        super().__init__(health, mana)
        self.damage = damage


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Spell:

    def __init__(self, name, damage, required_mana):
        self.name = name
        self.damage = damage
        self.required_mana = required_mana


class Dungeon:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != 0]
        self.dungeon = [[ch for ch in line] for line in lines]
        self.x = -1
        self.y = -1

    def print_map(self):
        for x in self.dungeon:
            ss = ''.join(x)
            print(ss)

    def spawn(self, hero):
        if not isinstance(hero, Hero):
            raise Exception("The hero must be from class Hero")
        self.hero = hero
        found = False
        for i in range(0, len(self.dungeon)):
            for j in range(0, len(self.dungeon[i])):
                if self.dungeon[i][j] == 'S':
                    self.dungeon[i][j] = 'H'
                    self.x = i
                    self.y = j
                    found = True
                    break
                if found:
                    break
        return found

    def move_up(self):
        check = True
        if self.y - 1 < 0:
            check = False
        elif self.dungeon[self.y - 1][self.x] == '.':
            temp = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = self.dungeon[self.y - 1][self.x]
            self.dungeon[self.y - 1][self.x] = temp
            self.y -= 1
        elif self.dungeon[self.y - 1][self.x] == '#':
            check = False
        elif self.dungeon[self.y - 1][self.x] == 'T':
            self.dungeon[self.y][self.x] = "."
            # absorb treasure
            self.dungeon[self.y - 1][self.x] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.y -= 1
        else:
            # Fight
            print("Let's fight")
        return check

    def move_down(self):
        check = True
        if self.y + 1 > len(self.dungeon) - 1:
            check = False
        elif self.dungeon[self.y + 1][self.x] == '.':
            temp = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = self.dungeon[self.y + 1][self.x]
            self.dungeon[self.y + 1][self.x] = temp
            self.y += 1
        elif self.dungeon[self.y + 1][self.x] == '#':
            check = False
        elif self.dungeon[self.y + 1][self.x] == 'T':
            # absorb treasure
            self.dungeon[self.y + 1][self.x] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.y += 1
        else:
            # Fight
            print("Let's fight")
        return check

    def move_left(self):
        check = True
        if self.x - 1 < 0:
            check = False
        elif self.dungeon[self.y][self.x - 1] == '.':
            temp = self.dungeon[self.y][self.x - 1]
            self.dungeon[self.y][self.x - 1] = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = temp
            self.x -= 1
        elif self.dungeon[self.y][self.x - 1] == '#':
            check = False
        elif self.dungeon[self.y][self.x - 1] == 'T':
            # absorb treasure
            self.dungeon[self.y][self.x - 1] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.x -= 1
        else:
            # Fight
            print("Let's fight")
        return check

    def move_right(self):
        check = True
        if self.x + 1 > len(self.dungeon[0]) - 1:
            check = False
        elif self.dungeon[self.y][self.x + 1] == ".":
            temp = self.dungeon[self.y][self.x + 1]
            self.dungeon[self.y][self.x + 1] = self.dungeon[self.y][self.x]
            self.dungeon[self.y][self.x] = temp
            self.x += 1
        elif self.dungeon[self.y][self.x + 1] == "#":
            check = False
        elif self.dungeon[self.y][self.x + 1] == 'T':
            # absorb treasure
            self.dungeon[self.y][self.x + 1] = 'H'
            self.dungeon[self.y][self.x] = "."
            self.x += 1
        else:
            # Fight
            print("Let's fight")
        return check

    def move_hero(self, direction):
        directions = ["up", "right", "down", "left"]
        if direction.lower() not in directions:
            raise Exception("Not a valid direction")
        elif direction.lower() == "up":
            self.move_left()
            self.mana += self.mana_regeneration_rate
        elif direction.lower() == "down":
            self.move_down()
            self.mana += self.mana_regeneration_rate
        elif direction.lower() == "right":
            self.move_right()
            self.mana += self.mana_regeneration_rate
        else:
            self.move_left()
            self.mana += self.mana_regeneration_rate

    def pick_treasure(self):
        weapon_bonus = Weapon("Spike", 25)
        spell_bonus = Spell("Silver", 30, 7)
        mana_bonus = 6
        health_potion_bonus = 10
        T = random.choice(
            [mana_bonus, health_potion_bonus, weapon_bonus, spell_bonus])
        if T == mana_bonus:
            self.hero.take_mana(mana_bonus)
        elif T == health_potion_bonus:
                self.hero.take_healing(health_potion_bonus)
        elif T == weapon_bonus:
            self.hero.equip(T)
        else:
            self.hero.learn(T)


map = Dungeon("textfile.txt")
map.print_map()
print("------------")
map.spawn()
# print(map.move_right())
# print("------------")
# map.print_map()
# print(map.move_down())
# print("------------")
# map.print_map()
# print(map.move_down())
# print("------------")
# map.print_map()
map.move_hero("Right")
map.print_map()
print("------------")
map.move_hero("Down")
map.print_map()
print("------------")
map.move_hero("Down")
map.print_map()
print("------------")
map.move_hero("Nagore")
