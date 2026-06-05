import pyxel
import time
pyxel.init(256, 256, title="Nuit du Code")

path = [(0, 128), (32, 128), (32, 0), (64, 0), (64, 256), (96, 256), (96, 256), (128, 256), (128, 0), (160, 0), (160, 256), (192, 256), (224, 256), (224, 128), (256, 128)]
class mob:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.speed = 1

    def move(self, dx, dy):
        for i in range path:
             

    def hurt(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self, wave):
        wave.mobs.remove(self)

    def draw(self):
        pyxel.cls(0)  
        pyxel.rect(self.x, self.y, 10, 10, 8)

    def update(self):
        if path:
            target_x, target_y = path[0]
            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx**2 + dy**2) ** 0.5
            if distance < self.speed:
                self.x, self.y = target_x, target_y
                path.pop(0)  
            else:
                self.move(dx / distance, dy / distance)

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

    def update(self):
        for mob in self.mobs:
            mob.update()

mob1 = mob(10, 10, 100)
mob2 = speedster(20, 20)
wave1 = wave([mob1, mob2])





 
pyxel.run(wave1.update, wave1.draw)