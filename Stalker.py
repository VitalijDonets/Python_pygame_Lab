import pygame

class Stalker:
    _texture = None
    _texture_path = None
    _fraction = None
    _max_health = None
    _max_armor = None
    _x = 0
    _y = 0
    _size = 75
    def __init__(self, name, rank):
        self._name = name
        self._rank = rank
        self._max_health = self._init_health()
        self._max_armor = self._init_armor()
        self._health = self._max_health
        self._armor = self._max_armor
        self._damage = self._init_damage()
        self._texture = pygame.image.load(self._texture_path)
        self._texture = pygame.transform.scale(self._texture, (self._size, self._size))
        self._reputation = {}

    def get_fraction(self):
        return self._fraction

    def __str__(self):
        info = ("Name: " + self._name + "\nFraction: " + self._fraction +
                "\nRank: " + str(self._rank) + "\nHealth: " + str(self._health) +
                "\nArmor: " + str(self._armor) + "\nDamage: " + str(self._damage))
        return info

    def get_size(self):
        return self._size

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def _init_health(self):
        if 0 <= self._rank <= 299:
            return 100 + 0.1 * self._rank
        elif 300 <= self._rank <= 599:
            return 200 + 0.2 * self._rank
        elif 600 <= self._rank <= 899:
            return 350 + 0.25 * self._rank
        else:
            return 500 + 0.3 * self._rank

    def _init_armor(self):
        if 0 <= self._rank <= 299:
            return 50 + 0.1 * self._rank
        elif 300 <= self._rank <= 599:
            return 150 + 0.2 * self._rank
        elif 600 <= self._rank <= 899:
            return 350 + 0.25 * self._rank
        else:
            return 600 + 0.3 * self._rank

    def _init_damage(self):
        if 0 <= self._rank <= 299:
            return 10 + 0.1 * self._rank
        elif 300 <= self._rank <= 599:
            return 25 + 0.2 * self._rank
        elif 600 <= self._rank <= 899:
            return 50 + 0.25 * self._rank
        else:
            return 100 + 0.3 * self._rank

    def _initTexturePath(self, rank, fraction):
        if 0 <= rank <= 299:
            self._texture_path = f"png/{fraction}1.png"
        elif 300 <= rank <= 599:
            self._texture_path = f"png/{fraction}2.png"
        elif 600 <= rank <= 899:
            self._texture_path = f"png/{fraction}3.png"
        else:
            self._texture_path = f"png/{fraction}4.png"

    def render(self, screen):
        screen.blit(self._texture, (self._x, self._y))

    def get_health(self):
        return self._health

    def change_life_params(self, param):
        if param < float(0):
            if self._armor > 0:
                self._armor += param
                if self._armor < 0:
                    self._health += self._armor
                    if self._health < 0:
                        self._health = 0
                    self._armor = 0
            else:
                self._health += param
                if self._health < 0:
                    self._health = 0
        elif param > float(0):
            if self._health == self._max_health:
                if self._armor < self._max_armor:
                    self._armor += param
                    if self._armor > self._max_armor:
                        self._armor = self._max_armor
            else:
                self._health += param
                if self._health > self._max_health:
                    self._armor = self._health - self._max_health
                    self._health = self._max_health

    def get_reputation(self, other_frac):
        return self._reputation[other_frac]

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def get_damage(self):
        return self._damage
#end class Stalker
