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


window = pg.display.set_mode((700, 500))
pg.display.set_caption('Maze')
background = pg.transform.scale(pg.image.load('background.jpg'), (700, 500))
pg.mixer.init()
pg.mixer.music.load('jungles.ogg')
pg.mixer.music.play()
game = True
FPS = 60
clock = pg.time.Clock()
hero = GameSprite('hero.png', 5, 420, 15)
cyborg = GameSprite('cyborg.png', 420, 280, 10)
treasure = GameSprite('treasure.png', 580, 420, 0)
while game:
    window.blit(background, (0, 0))
    hero.reset()
    treasure.reset()
    cyborg.reset()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
    pg.display.update()
    clock.tick(FPS)
