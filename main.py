"""
坦克大战游戏的需求
1。项目中有那些类
2.没个类中有那些方法

1.坦克类（我方坦克、地方坦克）
    射击
    移动类
    显示坦克的方法
2.子弹类
    移动类
    显示子弹的方法
3.墙壁类
    属性：是否可以通过
4.爆炸效果类
    展示爆炸效果
5.音效类
    播放音乐
6.主类
    开始游戏
    结束游戏

新增功能能
    加载主窗口
新增功能
    添加事件
    1.点击关闭窗口
    2.按下键盘时候，如果判断按下的是什么键，分别做不同的处理
"""
import pygame
import time

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class MainGame:
    windows = None
    my_tank = None

    def _init_(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.windows = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 初始化我方坦克
        MainGame.my_tank = Tank(350, 250)
        # 设置标题
        pygame.display.set_caption("坦克大战1.03")
        while True:
            time.sleep(0.02)
            # 给窗口设置一个填充色
            MainGame.windows.fill(BG_COLOR)
            self.getEvent()
            # 绘制文字
            MainGame.windows.blit(self.getTextSuface('地方坦克剩余数量%d' % 6), (10, 10))

            MainGame.my_tank.displayTank()
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()

            pygame.display.update()

    # 结束游戏
    def endGame(self):
        print('谢谢使用，欢迎再次使用')
        exit()

    # 左上角文字的绘制
    def getTextSuface(self, text):
        pygame.font.init()
        # 获取字体Font对象
        font = pygame.font.SysFont('kaiti', 18)
        # 绘制文字信息
        textSuface = font.render(text, True, TEXT_COLOR)
        return textSuface

    # 获取事件
    def getEvent(self):
        # 获取事件
        eventList = pygame.event.get()
        for event in eventList:
            # 判断按下的键是关闭还是键盘
            # 如果按的是推辞，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()
            # 如果是键盘的按下
            if event.type == pygame.KEYDOWN:
                # 判断按下的是上、下、左、右
                if event.key == pygame.K_LEFT:
                    # 切换方向
                    MainGame.my_tank.direction = 'L'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
                elif event.key == pygame.K_RIGHT:
                    MainGame.my_tank.direction = 'R'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
                elif event.key == pygame.K_UP:
                    MainGame.my_tank.direction = 'U'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
                elif event.key == pygame.K_DOWN:
                    MainGame.my_tank.direction = 'D'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
            if event.type == pygame.KEYUP:
                MainGame.my_tank.stop = True


class Tank:
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif'),
        }
        # 方向
        self.direction = 'L'
        # 根据当前图片的方向获取图片
        self.image = self.images[self.direction]
        # 获取区域
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 5
        self.stop = True

    # 移动
    def move(self):
        # 判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed

    # 射击
    def slot(self):
        pass

    # 展示坦克的方法
    def displayTank(self):
        # 获取展示对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.windows.blit(self.image, self.rect)


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 子弹类
class Bullet:
    def __init__(self):
        pass

    # 移动
    def move(self):
        pass

    # 展示子弹的方法
    def displayBullet(self):
        pass


# 地方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass


# 墙壁类
class Wall:
    def __init__(self):
        pass

    # 显示墙壁的方法
    def displayWall(self):
        pass


class Explode():
    def __init__(self):
        pass

    # 展示爆炸效果
    def displayExplode(self):
        pass


class Music:
    def __init__(self):
        pass

    # 播放音乐
    def playMusic(self):
        pass


if __name__ == "__main__":
    MainGame().startGame()
