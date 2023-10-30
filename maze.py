# создай игру "Лабиринт"!
import pygame as pg


class GameSprite(pg.sprite.Sprite):
    def __init__(self, picture, x, y, speed):
        super().__init__()
        self.picture = pg.transform.scale(pg.image.load(picture), (65, 65))
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pg.K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys[pg.K_d] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[pg.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed


class Enemy(GameSprite):     
    direction = 'left'
    def update(self):
        if self.rect.x < 470:
            self.direction = 'right'
        if self.rect.x > 615:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed



window = pg.display.set_mode((700, 500))
pg.display.set_caption('Maze')
background = pg.transform.scale(pg.image.load('background.jpg'), (700, 500))
pg.mixer.init()
pg.mixer.music.load('jungles.ogg')
pg.mixer.music.play()
game = True
FPS = 60
clock = pg.time.Clock()
hero = Player('hero.png', 5, 420, 15)
cyborg = Enemy('cyborg.png', 420, 280, 4)
treasure = GameSprite('treasure.png', 580, 420, 0)
while game:
    window.blit(background, (0, 0))
    hero.update()
    cyborg.update()
    hero.reset()
    treasure.reset()
    cyborg.reset()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
    pg.display.update()
    clock.tick(FPS)
