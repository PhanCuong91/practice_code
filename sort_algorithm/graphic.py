import pygame


class Graphic:

    white = (255, 255, 255)
    red = (255, 0, 0)

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.dis = None
        self.con = False

    def init_display(self):
        self.dis = pygame.display.set_mode((self.w, self.h))

    def draw_array(self, array, color):
        for i in range(len(array)):
            rect = ((i*2, 10),(1, array[i]*4))
            pygame.draw.rect(self.dis, color, rect)

    def run(self, color, array, con):
        while not con:
            self.dis.fill(color)
            self.draw_array(array, self.red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    quit()
        self.close()
        print("done")

    def close(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    quit()


gra = Graphic(320, 320)
gra.init_display()
gra.run(gra.white,[1,10,30],False)

