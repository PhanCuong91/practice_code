import pygame


class Graphic:
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    purple = (255, 0, 255)

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.dis = None
        self.con = False
        self.arr = []
        self.multi_height = 4
        self.width_bar = 9
        self.distance = self.width_bar + 1

    def init_display(self):
        self.dis = pygame.display.set_mode((self.w, self.h))

    def draw_array(self, array, color):
        for i in range(len(array)):
            rect = ((i*self.distance, 10), (self.width_bar, array[i]*self.multi_height))
            pygame.draw.rect(self.dis, color, rect)

    def draw_element(self, color, index, array):
        rect = ((index * self.distance, 10), (self.width_bar, array[index]*self.multi_height))
        pygame.draw.rect(self.dis, color, rect)

    def draw_bar_working_array(self, color, left, right):
        rect = ((left * self.distance, 0), ((right - left) * self.distance, 9))
        pygame.draw.rect(self.dis, color, rect)

    def run(self, color, array, key="None", dic_sort_alg=[]):
        # n = 0
        self.dis.fill(color)
        self.draw_array(array, self.red)
        # graphic for quick sort algorithm
        if 'quick_sort' == key:
            quick = dic_sort_alg['quick_sort']
            if len(quick) == 3:
                id_pivot = quick[0]
                left = quick[1]
                right = quick[2]
                # draw the pivot in display
                if id_pivot != -1:
                    self.draw_element(self.blue, id_pivot, array)
                # draw small array in display
                for i in range(left, id_pivot):
                    self.draw_element(self.green, i, array)
                # draw big array in display
                for i in range(id_pivot+1, right):
                    self.draw_element(self.yellow, i, array)
                # draw working array which is running quick_sort()
                self.draw_bar_working_array(self.purple, left, right)
        if 'merge_sort' == key:
            merge = dic_sort_alg['merge_sort']
            left = merge[0]
            m = merge[1]
            right = merge[2]
            if len(merge) == 3:
                for i in range(left, left+m):
                    self.draw_element(self.green, i, array)
                # draw big array in display
                for i in range(m+left, right):
                    self.draw_element(self.yellow, i, array)
                # draw working array which is running quick_sort()
                self.draw_bar_working_array(self.purple, left, right)
        if 'selection_sort' == key:
            selection = dic_sort_alg['selection_sort']
            sorted_array = selection[0]
            min_id = selection[1]
            s = selection[2]
            self.draw_array(sorted_array, self.green)
            self.draw_element(self.blue, min_id, array)
            self.draw_element(self.yellow, s, array)
        if 'bubble_sort' == key:
            bubble = dic_sort_alg['bubble_sort']
            left = bubble[0]
            right = bubble[1]
            self.draw_element(self.green, left, array)
            self.draw_element(self.yellow, right, array)
            self.draw_bar_working_array(self.purple, left, right+1)
        if 'insertion_sort' == key:
            insertion = dic_sort_alg[key]
            sorted_array = insertion[0]
            j = insertion[1]
            self.draw_array(sorted_array, self.blue)
            self.draw_element(self.yellow, j, array)
            self.draw_element(self.green, insertion[2], array)
        if key == 'heap_sort':
            heap = dic_sort_alg[key]
            if heap[3] == 0:
                self.draw_element(self.yellow, heap[0], array)
                self.draw_element(self.yellow, heap[1], array)
                self.draw_element(self.yellow, heap[2], array)
            if heap[3] == 1:
                self.draw_element(self.green, heap[0], array)
                self.draw_element(self.yellow, heap[1], array)
                self.draw_element(self.yellow, heap[2], array)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()


if __name__=="__main__":
    gra = Graphic(320, 320)
    gra.init_display()
    gra.run(gra.white, [1, 10, 30], False)

