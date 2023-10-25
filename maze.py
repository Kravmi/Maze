# создай игру "Лабиринт"!
import pygame as pg


class GameSprite(pg.sprite.Sprite):
    def __init__(self, picture, x, y, speed):
        super().__init__()
        self.picture = picture
        self.x = x
        self.y = y
        self.speed = speed


window = pg.display.set_mode((700, 500))
pg.display.set_caption('Maze')
background = pg.transform.scale(pg.image.load('background.jpg'), (700, 500))
pg.mixer.init()
pg.mixer.music.load('jungles.ogg')
pg.mixer.music.play()
game = True
FPS = 60
clock = pg.time.Clock()
while game:
    window.blit(background, (0, 0))
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
    pg.display.update()
    clock.tick(FPS)
