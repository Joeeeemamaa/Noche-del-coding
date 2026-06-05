import pyxel
pyxel.init(256, 256, title="Nuit du Code")

class mob:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = 1

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

    def hurt(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self, wave):
        wave.mobs.remove(self)

    def draw(self):
        pyxel.rect(self.x, self.y, 10, 10, 8)

    def get_position(self):
        return (self.x, self.y)


class mob1(mob):
    def __init__(self, x, y, hp, speed):
        super().__init__(x, y, hp)
        self.speed = speed

    def draw(self):
        pyxel.rect(self.x, self.y, 10, 10, 8)


class wave:    
    def __init__(self, mobs):
        self.mobs = mobs  

    def draw(self):
        for mob in self.mobs:
            mob.draw()

mob1 = mob(10, 10, 100)
wave1 = wave([mob1])




def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)
 
pyxel.run(update, draw)