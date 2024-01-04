import pygame

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
        self.rect.center = (10,H/2)
    
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

    def collide_color(self):
        pygame.sprite.Sprite.__init__(self)
        pixel = pygame.PixelArray(self.rect)
        apixel = pixel[self.rect.x:self.rect.x+self.rect.W,self.rect.y:self.rect.y+self.rect.H]
        pygame.PixelArray.close(pixel)
        return self.color in apixel

class start(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,480))# 起點大小
        self.image.fill(RED)#起點顏色
        self.rect = self.image.get_rect()
        self.rect.center = (10,H/2)

class end(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,480))# 起點大小
        self.image.fill(GREEN)#起點顏色
        self.rect = self.image.get_rect()
        self.rect.center = (710,H/2)

class backgroud:
    def __init__(self,screen,color,width,points):
        self.screen = screen
        self.color = color
        self.width = width
        self.points = points
        
            
    def draw(self):
        
        pygame.draw.lines(self.screen, self.color, False, self.points, self.width)
        for i in range(1,7):
            pygame.draw.rect(self.screen,self.color,[self.points[i][0]-14,self.points[i][1]-14,30,30],0)

            
    def add_point(self,point):
        self.points.append(point)

def collide_color(aSurface,aRect,aColor):
    pixel = pygame.PixelArray(aSurface)
    apixel = pixel[aRect.x:aRect.x+aRect.W,aRect.y:aRect.y+aRect.H]
    pygame.PixelArray.close(pixel)
    return aColor in apixel

wall = backgroud(screen,WHITE,thickness,[start_point])
wall.add_point(second_point)
wall.add_point(second_point2)
wall.add_point(third_point)
wall.add_point(third_point2)
wall.add_point(forth_point)
wall.add_point(forth_point2)
wall.add_point(end_point2)

all_sprites = pygame.sprite.Group()
Start = start()
End = end()
Player = Player()
all_sprites.add(Start,End,Player)

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
    wall.draw()
    all_sprites.draw(screen)

    if collide_color():
        print (f'GAME OVER')

    pygame.display.update()
pygame.quit()
