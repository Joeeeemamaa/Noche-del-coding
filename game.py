import pyxel

import time
pyxel.init(256, 256, title="Nuit du Code")
pyxel.mouse(True)
pyxel.load("theme.pyxres")

path = [
( 0 , 128 ), ( 4 , 128 ), ( 8 , 128 ), ( 12 , 128 ), ( 16 , 128 ), ( 20 , 128 ), ( 24 , 128 ), ( 28 , 128 ), ( 32 , 128 ), 
( 32 , 128 ), ( 32 , 124 ), ( 32 , 120 ), ( 32 , 116 ), ( 32 , 112 ), ( 32 , 108 ), ( 32 , 104 ), ( 32 , 100 ), ( 32 , 96 ), ( 32 , 92 ), ( 32 , 88 ), ( 32 , 84 ), ( 32 , 80 ), ( 32 , 76 ), ( 32 , 72 ), ( 32 , 68 ), ( 32 , 64 ), ( 32 , 60 ), ( 32 , 56 ), ( 32 , 52 ), ( 32 , 48 ), ( 32 , 44 ), ( 32 , 40 ), ( 32 , 36 ), ( 32 , 32 ), ( 32 , 28 ), ( 32 , 24 ), ( 32 , 20 ), ( 32 , 16 ), ( 32 , 12 ), ( 32 , 8 ), ( 32 , 4 ), 
( 32 , 0 ), ( 36 , 0 ), ( 40 , 0 ), ( 44 , 0 ), ( 48 , 0 ), ( 52 , 0 ), ( 56 , 0 ), ( 60 , 0 ), ( 64 , 0 ), 
( 64 , 0 ), ( 64 , 4 ), ( 64 , 8 ), ( 64 , 12 ), ( 64 , 16 ), ( 64 , 20 ), ( 64 , 24 ), ( 64 , 28 ), ( 64 , 32 ), ( 64 , 36 ), ( 64 , 40 ), ( 64 , 44 ), ( 64 , 48 ), ( 64 , 52 ), ( 64 , 56 ), ( 64 , 60 ), ( 64 , 64 ), ( 64 , 68 ), ( 64 , 72 ), ( 64 , 76 ), ( 64 , 80 ), ( 64 , 84 ), ( 64 , 88 ), ( 64 , 92 ), ( 64 , 96 ), ( 64 , 100 ), ( 64 , 104 ), ( 64 , 108 ), ( 64 , 112 ), ( 64 , 116 ), ( 64 , 120 ), ( 64 , 124 ), ( 64 , 128 ), ( 64 , 132 ), ( 64 , 136 ), ( 64 , 140 ), ( 64 , 144 ), ( 64 , 148 ), ( 64 , 152 ), ( 64 , 156 ), ( 64 , 160 ), ( 64 , 164 ), ( 64 , 168 ), ( 64 , 172 ), ( 64 , 176 ), ( 64 , 180 ), ( 64 , 184 ), ( 64 , 188 ), ( 64 , 192 ), ( 64 , 196 ), ( 64 , 200 ), ( 64 , 204 ), ( 64 , 208 ), ( 64 , 212 ), ( 64 , 216 ), ( 64 , 220 ), ( 64 , 224 ), ( 64 , 228 ), ( 64 , 232 ), ( 64 , 236 ), ( 64 , 240 ), ( 64 , 244 ), ( 64 , 248 ), 
( 64 , 250 ), ( 68 , 250 ), ( 72 , 250 ), ( 76 , 250 ), ( 80 , 250 ), ( 84 , 250 ), ( 88 , 250 ), ( 92 , 250 ), ( 96 , 250 ), 

( 96 , 250 ), ( 100 , 250 ), ( 104 , 250 ), ( 108 , 250 ), ( 112 , 250 ), ( 116 , 250 ), ( 120 , 250 ), ( 124 , 250 ), ( 128 , 250 ), 
( 128 , 250 ), ( 128 , 246 ), ( 128 , 242 ), ( 128 , 238 ), ( 128 , 234 ), ( 128 , 230 ), ( 128 , 226 ), ( 128 , 222 ), ( 128 , 218 ), ( 128 , 214 ), ( 128 , 210 ), ( 128 , 206 ), ( 128 , 202 ), ( 128 , 198 ), ( 128 , 194 ), ( 128 , 190 ), ( 128 , 186 ), ( 128 , 182 ), ( 128 , 178 ), ( 128 , 174 ), ( 128 , 170 ), ( 128 , 166 ), ( 128 , 162 ), ( 128 , 158 ), ( 128 , 154 ), ( 128 , 150 ), ( 128 , 146 ), ( 128 , 142 ), ( 128 , 138 ), ( 128 , 134 ), ( 128 , 130 ), ( 128 , 126 ), ( 128 , 122 ), ( 128 , 118 ), ( 128 , 114 ), ( 128 , 110 ), ( 128 , 106 ), ( 128 , 102 ), ( 128 , 98 ), ( 128 , 94 ), ( 128 , 90 ), ( 128 , 86 ), ( 128 , 82 ), ( 128 , 78 ), ( 128 , 74 ), ( 128 , 70 ), ( 128 , 66 ), ( 128 , 62 ), ( 128 , 58 ), ( 128 , 54 ), ( 128 , 50 ), ( 128 , 46 ), ( 128 , 42 ), ( 128 , 38 ), ( 128 , 34 ), ( 128 , 30 ), ( 128 , 26 ), ( 128 , 22 ), ( 128 , 18 ), ( 128 , 14 ), ( 128 , 10 ), ( 128 , 6 ), ( 128 , 2 ), 
( 128 , 0 ), ( 132 , 0 ), ( 136 , 0 ), ( 140 , 0 ), ( 144 , 0 ), ( 148 , 0 ), ( 152 , 0 ), ( 156 , 0 ), ( 160 , 0 ), 
( 160 , 0 ), ( 160 , 4 ), ( 160 , 8 ), ( 160 , 12 ), ( 160 , 16 ), ( 160 , 20 ), ( 160 , 24 ), ( 160 , 28 ), ( 160 , 32 ), ( 160 , 36 ), ( 160 , 40 ), ( 160 , 44 ), ( 160 , 48 ), ( 160 , 52 ), ( 160 , 56 ), ( 160 , 60 ), ( 160 , 64 ), ( 160 , 68 ), ( 160 , 72 ), ( 160 , 76 ), ( 160 , 80 ), ( 160 , 84 ), ( 160 , 88 ), ( 160 , 92 ), ( 160 , 96 ), ( 160 , 100 ), ( 160 , 104 ), ( 160 , 108 ), ( 160 , 112 ), ( 160 , 116 ), ( 160 , 120 ), ( 160 , 124 ), ( 160 , 128 ), ( 160 , 132 ), ( 160 , 136 ), ( 160 , 140 ), ( 160 , 144 ), ( 160 , 148 ), ( 160 , 152 ), ( 160 , 156 ), ( 160 , 160 ), ( 160 , 164 ), ( 160 , 168 ), ( 160 , 172 ), ( 160 , 176 ), ( 160 , 180 ), ( 160 , 184 ), ( 160 , 188 ), ( 160 , 192 ), ( 160 , 196 ), ( 160 , 200 ), ( 160 , 204 ), ( 160 , 208 ), ( 160 , 212 ), ( 160 , 216 ), ( 160 , 220 ), ( 160 , 224 ), ( 160 , 228 ), ( 160 , 232 ), ( 160 , 236 ), ( 160 , 240 ), ( 160 , 244 ), ( 160 , 248 ), 
( 160 , 250 ), ( 164 , 250 ), ( 168 , 250 ), ( 172 , 250 ), ( 176 , 250 ), ( 180 , 250 ), ( 184 , 250 ), ( 188 , 250 ), ( 192 , 250 ), 
( 192 , 250 ), ( 196 , 250 ), ( 200 , 250 ), ( 204 , 250 ), ( 208 , 250 ), ( 212 , 250 ), ( 216 , 250 ), ( 220 , 250 ), ( 224 , 250 ), 
( 224 , 250 ), ( 224 , 246 ), ( 224 , 242 ), ( 224 , 238 ), ( 224 , 234 ), ( 224 , 230 ), ( 224 , 226 ), ( 224 , 222 ), ( 224 , 218 ), ( 224 , 214 ), ( 224 , 210 ), ( 224 , 206 ), ( 224 , 202 ), ( 224 , 198 ), ( 224 , 194 ), ( 224 , 190 ), ( 224 , 186 ), ( 224 , 182 ), ( 224 , 178 ), ( 224 , 174 ), ( 224 , 170 ), ( 224 , 166 ), ( 224 , 162 ), ( 224 , 158 ), ( 224 , 154 ), ( 224 , 150 ), ( 224 , 146 ), ( 224 , 142 ), ( 224 , 138 ), ( 224 , 134 ), ( 224 , 130 ), 
( 224 , 128 ), ( 228 , 128 ), ( 232 , 128 ), ( 236 , 128 ), ( 240 , 128 ), ( 244 , 128 ), ( 248 , 128 )
]

class game:
    def __init__(self):
        self.towers = []
        self.waves = []
        self.current_wave = 1
        self.player = player()

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
            tower.update(self.waves[self.current_wave], self.player)
        self.place_tower(self.player)
        self.waves.append(self.create_wave(self.current_wave))
        pyxel.text(5, 5, f"Health: {self.player.health}", 7)
        pyxel.text(5, 15, f"Money: {self.player.money}", 7)


    def place_tower(self, player):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if player.spend_money(5):
                new_tower = tower(pyxel.mouse_x, pyxel.mouse_y)
                self.add_tower(new_tower)
        if pyxel.btnp(pyxel.KEY_0):
            if player.spend_money(10):
                new_tower = tanks_tower(pyxel.mouse_x, pyxel.mouse_y)
            self.add_tower(new_tower)
        if pyxel.btnp(pyxel.KEY_1):
            if player.spend_money(15):
                new_tower = sniper_tower(pyxel.mouse_x, pyxel.mouse_y)
                self.add_tower(new_tower)
        if pyxel.btnp(pyxel.KEY_2):
            if player.spend_money(20):
                new_tower = money_tower(pyxel.mouse_x, pyxel.mouse_y)
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
                if path[self.i][0] < path[self.i + 1][0]:
                    for j in range(path[self.i][0], path[self.i + 1][0], self.speed):
                        self.x = j
                else:
                    for j in range(path[self.i][0], path[self.i + 1][0], -self.speed):
                        self.x = j
            if path[self.i][1] != path[self.i + 1][1]:
                if path[self.i][1] < path[self.i + 1][1]:
                    for j in range(path[self.i][1], path[self.i + 1][1], self.speed):
                        print("+", j)
                        self.y = j
                else:
                    for j in range(path[self.i][1], path[self.i + 1][1], -self.speed):
                        print("-", j)
                        self.y = j


    def hurt(self, damage, wave):
        self.hp -= damage
        if self.hp <= 0:
            self.die(wave)

    def die(self, wave):
        wave.mobs.remove(self)

    def draw(self):
        pyxel.cls(5)
        pyxel.blt(self.x, self.y, 0, 16, 8, 8, 8, 2)

    def update(self):
        self.move()
        if pyxel.btn(pyxel.KEY_SPACE):
            self.hurt(10)

    def get_position(self):
        return (self.x, self.y)


class speed_mob(mob):
    def __init__(self, x, y):
        super().__init__(x, y, 50)
        self.speed = 3

    def die(self, wave):
        print("Speedster eel died")
        super().die(wave)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 23, 0, 8, 8, 2)

class tank_mob(mob):
    def __init__(self, x, y):
        super().__init__(x, y, 150)
        self.speed = 0.5

    def die(self, wave):
        print("Resistant jellyfish died")
        super().die(wave)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 8, 16, 16, 2)

class elite_mob(mob):
    def __init__(self, x, y):
        super().__init__(x, y, 150)
        self.speed = 1

    def die(self, wave):
        print("Elite whale died")
        super().die(wave)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 12, 32, 32, 32, 2)



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
        self.cd = 5
        self.range = 50
        self.damage = 10


    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 2)

    def update(self, wave, player):
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
        self.cd = 10
        self.range = 50
        self.damage = 5

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32, 16, 16, 2)

    def update(self, wave, player):
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
        self.cd = 15
        self.range = 100
        self.damage = 15

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 48, 16, 16, 2)

    def update(self, wave, player):
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

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        return False



Game = game()





 
pyxel.run(Game.update, Game.draw)


