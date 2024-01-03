import pygame
import random
FPS = 60
W = 720
H = 480

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

speedx = 2
speedy = 2
start_point = (20,240)
end_point = (700,240)
second_point = (200,240)
second_point2 = (200,75)
third_point = (500,75)
third_point2 = (500,200)
forth_point = (600,200)
forth_point2 = (600,240)
end_point2 = (700,240)

thickness = 30

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((W, H))#視窗高低
clock = pygame.time.Clock()
pygame.display.set_caption("電流急急棒")#標題

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))# 角色大小
        self.image.fill(BLUE)#角色顏色
        self.rect = self.image.get_rect()
        self.rect.center = (W/2,H/2)
    #讓角色移動
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x +=speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -=speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y -= speedy
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += speedy
        if self.rect.right > W:
            self.rect.right = W
        if self.rect.left  < 0 :
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > H:
            self.rect.bottom = H

class backgroud:
    def __init__(self,screen,color,width,points):
        self.screen = screen
        self.color = color
        self.width = width
        self.points = points

    def draw(self):
        square = pygame.Surface((30, 30))
        square.fill(self.color)
        square_rect = square.get_rect(center=(self.points[0][1],self.points[0][0]))
        pygame.draw.lines(self.screen, self.color, False, self.points, self.width)
        print (self.points)

    def add_point(self,point):
        self.points.append(point)

wall = backgroud(screen,WHITE,thickness,[start_point])
wall.add_point(second_point)
wall.add_point(second_point2)
wall.add_point(third_point)
wall.add_point(third_point2)
wall.add_point(forth_point)
wall.add_point(forth_point2)
wall.add_point(end_point2)

all_sprites = pygame.sprite.Group()
Player = Player()
all_sprites.add(Player)

#遊戲迴圈
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #更新遊戲
    all_sprites.update()

    #顯示畫面
    screen.fill(BLACK) 
    all_sprites.draw(screen)
    wall.draw()
    pygame.display.update()
pygame.quit()
