import pygame
import random
FPS = 60
W = 720
H = 480

BLACK = (0,0,0)
WRITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

speedx = 5
speedy = 5
start_point = (20,240)
end_point = (700,240)
max_turn_angle = 90
max_length = 200
thickness = 30

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((W, H))#視窗高低
clock = pygame.time.Clock()
pygame.display.set_caption("電流急急棒")#標題

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (W/2,H/2)
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
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.center = (360,240)
        self.radius = 5
        self.start_angle = 0
        self.end_angle = 90

class Line(pygame.sprite.Sprite):
    def __init__(self, start_point, end_point, max_turn_angle, max_length, thickness, color):
        super().__init__()
        self.start_point = start_point
        self.end_point = end_point
        self.max_turn_angle = max_turn_angle
        self.max_length = max_length
        self.thickness = thickness
        self.color = WRITE

    def update(self):
        pass

    def draw(self, screen):
        # 計算線條的點列表
        points = []
        points.append(self.start_point)
        while points[-1] != self.end_point:
            # 計算下一個點的座標
            next_point = points[-1] + (random.randint(-10, 10), random.randint(-10, 10))

            # 如果下一個點不在螢幕內，則返回起點
            if next_point[0] < 0 or next_point[0] > W or next_point[1] < 0 or next_point[1] > H:
                next_point = self.start_point

            # 計算下一個點的角度
            next_angle = random.randint(0, 360)

            # 如果角度太大，則調整角度
            if abs(next_angle - points[-1][0]) > self.max_turn_angle:
                next_angle = points[-1][0] + (random.randint(-30, 30))

            # 將下一個點新增到點列表
            points.append((next_point[0], next_point[1]))

all_sprites = pygame.sprite.Group()
Player = Player()
Line = Line(start_point,end_point,max_turn_angle,max_length,thickness,WRITE)
all_sprites.add(Player,Line)

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
    pygame.display.update()
pygame.quit()
