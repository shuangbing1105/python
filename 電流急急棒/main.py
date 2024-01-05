import pygame
FPS = 60
W = 720
H = 480

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
#速度
speed = 3
speedx = speedy = speed

start_point = (20,240)
end_point = (700,240)
second_point = (200,240)
second_point2 = (200,75)
third_point = (500,75)
third_point2 = (500,200)
forth_point = (600,200)
forth_point2 = (600,240)
end_point2 = (700,240)

thickness = 30#設定走道寬度

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((W, H))#視窗高低
clock = pygame.time.Clock()
pygame.display.set_caption("電流急急棒")#標題
#初始畫面定義
def draw_init():
    draw_text(screen, "Press up,down,left,right to move", 32, W/2, H/2)
    draw_text(screen, "Press any key to continue", 18, W/2, H*3/4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running,system_speed
                waiting = False
                running = False
                system_speed = False
                pygame.quit()
            elif event.type == pygame.KEYUP:
                waiting = False
                running = True
#顯示文字在畫面上
def draw_text(surf,text,size,x,y):
    font = pygame.font.SysFont("SimHei",size)
    text_surface = font.render(text,True,WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surf.blit(text_surface,text_rect)
#遊戲結束
def GAMEOVER():
    global move,running
    pygame.draw.rect(screen,BLACK,[0,0,720,480])
    move = False
    draw_text(screen, "GAME OVER", 64, W/2, H/2)
    running = False
#遊戲成功
def SUCCESS():
    global move,running
    pygame.draw.rect(screen,BLACK,[0,0,720,480])
    move = False
    draw_text(screen, "SUCCESS", 64, W/2, H/2)
    running = False
#角色
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))# 角色大小
        self.image.fill(BLUE)#角色顏色
        self.rect = self.image.get_rect()
        self.rect.center = (10,H/2)
    
    #讓角色移動
    def update(self):
        if move:
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
    def collide_inside(self):
        a = (self.rect.left < second_point[0]-(thickness/2-1) and self.rect.right > start_point[0] and self.rect.top <second_point[1]-(thickness/2)-1)
        b = (self.rect.left < third_point[0]+(thickness/2+1) and self.rect.right > second_point[0] and self.rect.top <third_point[1]-(thickness/2)-1)
        c = (self.rect.left < forth_point[0]+(thickness/2+1) and self.rect.right > third_point[0]+(thickness/2+1) and self.rect.top <forth_point[1]-(thickness/2)-1)
        d = (self.rect.left < end_point[0]-(thickness/2-1) and self.rect.right > forth_point[0]+(thickness/2+1) and self.rect.top <end_point[1]-(thickness/2)-1)
        e = (self.rect.left < second_point[0] and self.rect.right > start_point[0]+(thickness/2+1) and self.rect.bottom >second_point[1]+(thickness/2)+1)
        f = (self.rect.left < third_point[0]-(thickness/2-1) and self.rect.right > second_point[0]+(thickness/2+1) and self.rect.bottom >third_point[1]+(thickness/2)+1)
        g = (self.rect.left < forth_point[0]-(thickness/2-1) and self.rect.right > third_point[0]-(thickness/2-1) and self.rect.bottom >forth_point[1]+(thickness/2)+1)
        h = (self.rect.left < end_point[0] and self.rect.right > forth_point[0]-(thickness/2-1) and self.rect.bottom >end_point[1]+(thickness/2)+1)
        if (a or b or c or d or e or f or g or h):
            return True
        
    def collide_win(self):
        if (self.rect.left >= 700):
            return True
#起點線
class start(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,480))# 起點大小
        self.image.fill(RED)#起點顏色
        self.rect = self.image.get_rect()
        self.rect.center = (10,H/2)
#終點線
class end(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,480))# 起點大小
        self.image.fill(GREEN)#起點顏色
        self.rect = self.image.get_rect()
        self.rect.center = (710,H/2)
#走道
class backgroud:
    def __init__(self,screen,color,width,points):
        self.screen = screen
        self.color = color
        self.width = width
        self.points = points
        
            
    def draw(self):
        
        pygame.draw.lines(self.screen, self.color, False, self.points, self.width)#畫線
        for i in range(1,7):#因為線與線相交會缺一繳，所以要多畫一個點去彌補缺角
            pygame.draw.rect(self.screen,self.color,[self.points[i][0]-(self.width/2-1),self.points[i][1]-(self.width/2-1),self.width,self.width],0)

            
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
Start = start()
End = end()
Player = Player()
all_sprites.add(Start,End,Player)

#起始畫面
show_init = True
if show_init:
    draw_init()
    show_init = False
#遊戲主程式
move = True
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
    if Player.collide_inside():
        GAMEOVER()
    if Player.collide_win():
        SUCCESS()
    pygame.display.update()
pygame.time.wait(1000)
pygame.quit
