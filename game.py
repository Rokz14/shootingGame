import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Shooting game")
clock = pygame.time.Clock()

class Player(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 10
        # self.isJump = False
        # self.left = False
        # self.right = False
        # self.walkCount = 0
        # self.jumpCount = 10

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        
class Enemy(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.hitbox = (self.x, self.y, + self.width, self.height)

    def draw(self, win):
        self.hitbox = (self.x, self.y, + self.width, self.height)
        # pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, (0, 255, 0), self.hitbox)

    def hit(self):
        print('hit')

class Projectile(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def redrawGameWindow():
    win.fill((0, 0, 0))
    man.draw(win)
    ork.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

man = Player(230,440,60,40)
bullets = []
ork = Enemy(random.randint(0, 460), -60, 60, 40)
orks = [ork]

run = True
while run:

    # pygame.time.delay(30)
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for ork in orks:
        if ork.y < 500 and ork.y >= -60:
            ork.y += ork.vel    
        else:
            orks.pop(orks.index(ork))
            orks.append(Enemy(random.randint(0, 460), -60, 60, 40))

    for bullet in bullets:
        if bullet.y - bullet.radius < ork.hitbox[1] + ork.hitbox[3] and bullet.y + bullet.radius > ork.hitbox[1]:
            if bullet.x + bullet.radius > ork.hitbox[0] and bullet.x - bullet.radius < ork.hitbox[0] + ork.hitbox[2]:
                ork.hit()
                orks.pop(orks.index(ork))
                orks.append(Enemy(random.randint(0, 460), -60, 60, 40))
                bullets.pop(bullets.index(bullet))
        if bullet.y < 500 and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # for bullet in bullets:
    #     if bullet.y < 500 and bullet.y > 0:
    #         bullet.y -= bullet.vel
    #     else:
    #         bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 10:
            bullets.append(Projectile(round(man.x + man.width //2), round(man.y), 6, (255,0,0)))
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width:
        man.x += man.vel
    if keys[pygame.K_UP] and man.y > 0:
        man.y -= man.vel
    if keys[pygame.K_DOWN] and man.y < 500 - man.height:
        man.y += man.vel

    # if keys[pygame.K_m]:
    #     orks.append(Enemy(random.randint(0, 460), -60, 60, 40))
    
    redrawGameWindow()

pygame.quit()
