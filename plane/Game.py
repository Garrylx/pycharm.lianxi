import sys,pygame

class Settings():#创建设置类，把有可能需要修改的放进去
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 652
        self.bg_color = (187,255,255)#使用RGB颜色对照表
        self.h_speed = 2

        self.bl_speed = 6


class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,Settings,hero):
        super(Bullet,self).__init__()
        self.screen = screen
        self.Settings = Settings
        self.hero = hero
        self.image = pygame.image.load("D:/python资料/代码/image/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = hero.rect.centerx
        self.rect.y = hero.rect.y
        self.y = float(hero.rect.y)
        self.speed = Settings.bl_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def update_bl(self,bullets):
        bullets.update()
        for bl in bullets.sprites():
            if bl.rect.bottom < 0:
                bullets.remove(bl)

    def blit_me(self):
        self.screen.blit(self.image, self.rect)


class Bg():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("D:/python资料/代码/image/background.png")#加载图片 +路径
        self.rect = self.image.get_rect()


    def blit_me(self):
        self.screen.blit(self.image,self.rect)


class Hero():
    def __init__(self,screen,settings):
        self.screen = screen
        self.image = pygame.image.load("D:/python资料/代码/image/hero1.png")
        self.rect = self.image.get_rect()#获得图片位置信息
        self.screen_rect = self.screen.get_rect()#获得位置信息
        self.rect.centerx = self.screen_rect.centerx#确认初始位置
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.settings = settings


    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:#或者if self,moving_right
            self.rect.centerx += self.settings.h_speed
        if self.moving_right == False:
            pass
        if self.moving_left == True and self.rect.left > 0:#或者if self,moving_right
            self.rect.centerx -= self.settings.h_speed
        if self.moving_left == False:
            pass



    def blit_me(self):
        self.screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen,Settings):
        super(Enemy,self).__init__()
        self.screen = screen
        self.Settings = Settings
        self.image = pygame.image.load("D:/python资料/代码/image/enemy1.png")
        self.rect = self.image.get_rect()

        self.rect.x = 10
        self.rect.y = 10


    def blit_me(self):
        self.screen.blit(self.image, self.rect)


def check_events(screen,hero,Settings,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = True
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True
            elif event.key == pygame.K_SPACE:
                bullet1 = Bullet(screen,Settings,hero)
                bullets.add(bullet1)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = False
            elif event.key == pygame.K_LEFT:
                hero.moving_left = False


def update_screen(bg,hero,bullets,enemy,screen):
    bg.blit_me()
    for bullet in bullets.sprites():
        bullet.blit_me()
    hero.blit_me()
    enemy.blit_me()
    pygame.display.flip()  # 屏幕刷新

"""def create_enemys(enemys,screen,Settings):
    enemy = Enemy(screen,Settings)
    num_enemy = screen.get_rect().width/(20+enemy.rect.width)
    for index in range(num_enemy):
        if index == 0:
            continue
        x = 10 + index*(20+enemy.rect.width)
        new_ene = Enemy(screen.Settings)
        new_ene.rect.x = x
        enemys.add(new_ene)
"""


def run_game():
    pygame.init()#初始化
    setting = Settings()#调用setting类
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))#创建可视窗口并设置大小分辨率

    bg = Bg(screen)#调用Bg类
    hero = Hero(screen,setting)#调用hero类
    enemy = Enemy(screen,Settings)
    bullets = pygame.sprite.Group()


    while True:
        check_events(screen,hero,setting,bullets)
        hero.update()
        Bullet.update_bl(bullets,bullets)
        update_screen(bg, hero,bullets,enemy,screen)


    #bg_rect = bg.get_rect()#得到位置坐标
    #rect(x,y,width,height)  rect含有四个元素
    #my_rect = pygame.Rect(0,0,0,0)
    # 游戏元素居中
    #center、centerx、centery  可用于修改位置
    # 游戏元素与屏幕边缘对齐
    #top、bottom、left、right    可用于修改位置

    #原点（0，0）位于屏幕的左上方，向右下方移动时，坐标值增大。
    #rect对象的各个属性只能存储 整数 值。



#run_game()


    """
    while True:#创建死循环，一直监测输入端操作

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit")
                pygame.quit()
                sys.exit()
    """
            #代码重构前
            #screen.fill(setting.bg_color)  # 屏幕填充颜色，并覆盖之前的画面
            #screen.blit(bg,my_rect)#得到图片，并确定绘制位置
            #screen.blit(bg,bg_rect)
            # 绘制主角


run_game()
