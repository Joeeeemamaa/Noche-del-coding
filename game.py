import pyxel

import time
pyxel.init(256, 256, title="Nuit du Code")
pyxel.mouse(True)
pyxel.load("theme.pyxres")

path = [(0, 128), (32, 128), (32, 0), (64, 0), (64, 256), (96, 256), (96, 256), (128, 256), (128, 0), (160, 0), (160, 256), (192, 256), (224, 256), (224, 128), (256, 128)]


class game:
    def __init__(self):
        self.towers = []
        self.waves = []
        self.current_wave = 1

    def add_tower(self, tower):
        self.towers.append(tower)

    def add_wave(self, wave):
        self.waves.append(wave)

    def update(self):
        if self.current_wave < len(self.waves):
            current_wave = self.waves[self.current_wave]
            current_wave.update()
            if not current_wave.mobs:
                self.current_wave += 1
        for tower in self.towers:
            tower.update(self.waves[self.current_wave])
        self.place_tower()
        self.waves.append(self.create_wave(self.current_wave))

    def place_tower(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            new_tower = tower(pyxel.mouse_x, pyxel.mouse_y)
            self.add_tower(new_tower)

    def draw(self):
        if self.current_wave < len(self.waves):
            current_wave = self.waves[self.current_wave]
            current_wave.draw()
        for tower in self.towers:
            tower.draw()
    

    def create_wave(self, wave_number):
        mobs = []
        for i in range(wave_number * 5):
            mobs.append(mob(0, 128, 100))
        return wave(mobs)



class mob:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.pathmax = len(path) - 1
        self.i = 0
        self.speed = 1

    def move(self):
        if pyxel.frame_count%10 == 0:
            self.i += 1

        if self.i < self.pathmax:
            if path[self.i][0] != path[self.i + 1][0]:
                for j in range(path[self.i][0], path[self.i + 1][0], self.speed):
                    self.x = j
            if path[self.i][1] != path[self.i + 1][1]:
                if path[self.i][1] < path[self.i + 1][1]:
                    for j in range(path[self.i][1], path[self.i + 1][1], self.speed):
                        #print("+", j)
                        self.y = j
                else:
                    for j in range(path[self.i][1], path[self.i + 1][1], -self.speed):
                        #print("-0", j)
                        self.y = j
            

    def hurt(self, damage, wave):
        self.hp -= damage
        if self.hp <= 0:
            self.die(wave)

    def die(self, wave):
        wave.mobs.remove(self)

    def draw(self):
        pyxel.cls(0)  
        pyxel.blt(self.x, self.y, 0, 16, 32, 32, 32, 2)

    def update(self):
        self.move()
        if pyxel.btn(pyxel.KEY_SPACE):
            self.hurt(10)

    def get_position(self):
        return (self.x, self.y)


class speedster(mob):
    def __init__(self, x, y):
        super().__init__(x, y, 50)
        self.speed = 3

    def die(self, wave):
        print("Speedster died")
        super().die(wave)

    def draw(self):
        pyxel.rect(self.x, self.y, 10, 10, 8)



class wave:    
    def __init__(self, mobs):
        self.mobs = mobs  

    def draw(self):
        for mob in self.mobs:
            mob.draw()

    def update(self):
        for mob in self.mobs:
            mob.update()


class tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.price = 5
        self.cd = 10
        self.range = 50
        self.damage = 10


    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 2)

    def update(self, wave):
        for mob in wave.mobs:
            if self.in_range(mob) and (pyxel.frame_count % self.cd == 0):
                mob.hurt(self.damage, wave)

    def in_range(self, mob):
        mob_x, mob_y = mob.get_position()
        distance = ((self.x - mob_x) ** 2 + (self.y - mob_y) ** 2) ** 0.5
        return distance <= self.range

class tanks_tower (tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.price = 10
        self.cd = 20
        self.range = 50
        self.damage = 5

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32, 16, 16, 2)

    def update(self, wave):
        for mob in wave.mobs:
            if self.in_range(mob) and (pyxel.frame_count % self.cd == 0):
                mob.hurt(self.damage, wave)

    def in_range(self, mob):
        mob_x, mob_y = mob.get_position()
        distance = ((self.x - mob_x) ** 2 + (self.y - mob_y) ** 2) ** 0.5
        return distance <= self.range

class sniper_tower (tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.price = 15
        self.cd = 30
        self.range = 100
        self.damage = 15

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 48, 16, 16, 2)

    def update(self, wave):
        for mob in wave.mobs:
            if self.in_range(mob) and (pyxel.frame_count % self.cd == 0):
                mob.hurt(self.damage, wave)

    def in_range(self, mob):
        mob_x, mob_y = mob.get_position()
        distance = ((self.x - mob_x) ** 2 + (self.y - mob_y) ** 2) ** 0.5
        return distance <= self.range

class money_tower (tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.price = 20
        self.cd = 30
        self.range = 0
        self.damage = 0

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 64, 16, 16, 2)

    def update(self, wave, player):
        for mob in wave.mobs:
            if self.in_range(mob):
                mob.hurt(self.damage, wave)
        self.create_money(player)

    def create_money(self, player):
        if (pyxel.frame_count % self.cd == 0):
            player.earn_money(5)


    def in_range(self, mob):
        mob_x, mob_y = mob.get_position()
        distance = ((self.x - mob_x) ** 2 + (self.y - mob_y) ** 2) ** 0.5
        return distance <= self.range
    

class player:
    def __init__(self):
        self.health = 100
        self.money = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
    
    def die(self):
        print("Game Over")
        pyxel.quit()

    def earn_money(self, amount):
        self.money += amount




Game = game()

mob1 = mob(10, 10, 100)
mob2 = speedster(20, 20)
wave1 = wave([mob1, mob2])





 
pyxel.run(Game.update, Game.draw)


