from pygame import *
class GameSprite (sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, saiz_x, saiz_y, player_speed) :
        super().__init__()
        self.image = transform. scale(image. load(player_image), (saiz_x, saiz_y))
        self.speed = player_speed
        self.rect = self.image.get_rect ()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset (self):
        window.blit(self.image, (self.rect.x, self.rect.y))
window = display.set_mode((700, 500))
display.set_caption("шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
run = True 
FPS = 60
clock = time.Clock()
    #музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets .add(bullet)
lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0
            lost = lost + 1
from random import randint 
skip = Player("rocket.png", 300, 400, 80, 100, 10)
bullets = sprite.Group()
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy("asteroid.png", randint(80, 620), -40, 80, 50, randint(1, 5))
    monsters.add(monster)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
    
score = 0
font.init()
font1 = font.SysFont("Arial", 70)
win = font1.render('YOU WON', True, (0, 255, 0) )
lose = font1.render('YOU LOSE', True, (255, 0 , 0) )
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                skip.fire()
    if not finish:
        

        window.blit (background, (0, 0))
        text = font1.render("Счет:" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lost = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lost, (10, 50))
        skip.update()
        monsters.update()

        skip.reset()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy("ufo.png", randint(80, 700 - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        if lost > 10:
            finish = True
            window.blit(lose, (200, 200))
        if score > 10:
            finish = True
            window.blit(win, (200, 200))
        display.update()
    clock.tick(FPS)


