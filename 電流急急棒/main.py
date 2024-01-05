import pygame

FPS = 60
W = 720
H = 480

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

speedx = 1
speedy = 1
start_point = (20,240)
end_point = (700,240)
second_point = (200,240)
second_point2 = (200,75)
third_point = (500,75)
third_point2 = (500,200)
forth_point = (600,200)
forth_point2 = (600,240)
end_point2 = (700,240)

thickness = 25

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
    #判定主角是否出界
    def collide(self):
        a = (self.rect.left < second_point[0]-(thickness/2-1) and self.rect.right > start_point[0] and self.rect.top <second_point[1]-(thickness/2)-1)
        b = (self.rect.left < third_point[0]-(thickness/2-1) and self.rect.right > second_point[0] and self.rect.top <third_point[1]-(thickness/2)-1)
        c = (self.rect.left < forth_point[0]-(thickness/2-1) and self.rect.right > third_point[0]+(thickness/2+1) and self.rect.top <forth_point[1]-(thickness/2)-1)
        d = (self.rect.left < end_point[0]-(thickness/2-1) and self.rect.right > forth_point[0]+(thickness/2+1) and self.rect.top <end_point[1]-(thickness/2)-1)
        if (a or b or c or d ):
            print ("test")
        e = (self.rect.left < second_point[0] and self.rect.right > start_point[0]+(thickness/2+1) and self.rect.bottom >second_point[1]+(thickness/2)+1)
        f = (self.rect.left < third_point[0]-(thickness/2-1) and self.rect.right > second_point[0]+(thickness/2+1) and self.rect.bottom >third_point[1]+(thickness/2)+1)
        g = (self.rect.left < forth_point[0]-(thickness/2-1) and self.rect.right > third_point[0]-(thickness/2-1) and self.rect.bottom >forth_point[1]+(thickness/2)+1)
        h = (self.rect.left < end_point[0] and self.rect.right > forth_point[0]-(thickness/2-1) and self.rect.bottom >end_point[1]+(thickness/2)+1)
        if (e or f or g or h):
            print ("e")
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
            pygame.draw.rect(self.screen,self.color,[self.points[i][0]-(self.width/2-1),self.points[i][1]-(self.width/2-1),self.width,self.width],0)

            
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
    Player.collide()
    #    print (f'GAME OVER')

    pygame.display.update()
pygame.quit()
