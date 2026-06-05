import pyxel
pyxel.init(256, 256, title="Nuit du Code")

path = [(128, 0), (128, 8), (128, 16), (128,24), (136,24), (144,24), (152,24), (160,24), (168,24), (176,24), (184,24), (192,24), (200,24), (208,24), (208,32)]

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


class speedster(mob):
    def __init__(self, x, y):
        super().__init__(x, y, 50)
        self.speed = 3

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