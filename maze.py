# создай игру "Лабиринт"!
import pygame as pg
import constant as const


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


class Wall(pg.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = pg.display.set_mode((700, 500))
pg.display.set_caption('Maze')
background = pg.transform.scale(pg.image.load('background.jpg'), (700, 500))
pg.mixer.init()
pg.mixer.music.load('jungles.ogg')
pg.mixer.music.play()
game = True
clock = pg.time.Clock()
hero = Player('hero.png', 5, 420, 10)
cyborg = Enemy('cyborg.png', 420, 280, 4)
treasure = GameSprite('treasure.png', 580, 420, 0)
wall_1 = Wall(const.GREEN, 400, 10, 100, 50)
wall_2 = Wall(const.GREEN, 10, 355, 100, 50)
wall_3 = Wall(const.GREEN, 10, 300, 410, 160)
wall_4 = Wall(const.GREEN, 200, 10, 100, 250)
finish = False
pg.font.init()
font = pg.font.Font(None, 70)
win = font.render('YOU WIN!!!', True, const.YELLOW)
lose = font.render('YOU LOSE!!!', True, const.RED)
money = pg.mixer.Sound('money.ogg')
kick = pg.mixer.Sound('kick.ogg')
while game:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        wall_1.draw()
        wall_2.draw()
        wall_3.draw()
        wall_4.draw()
        hero.update()
        cyborg.update()
        hero.reset()
        treasure.reset()
        cyborg.reset()

        if pg.sprite.collide_rect(hero, treasure):
            finish = True
            window.blit(win, (200, 200))
            money.play()

        for obj in [wall_1, wall_2, wall_3, cyborg]:
            if pg.sprite.collide_rect(hero, obj):
                finish = True
                window.blit(lose, (200, 200))
                kick.play()

    pg.display.update()
    clock.tick(const.FPS)
