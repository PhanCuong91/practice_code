import random
import timeit
from threading import Thread
from time import sleep
import pygame


class SortAlgorithm:
    def __init__(self, n=0, rag=100):
        """
        :param n: number of array
        :param rag: range of array element
        """
        self.n = n
        self.range = rag
        self.array = []
        self.time = 0

    def get_timer(self):
        """
        :return: time when this function is called from beginning
        """
        return timeit.default_timer()

    def random_array(self):
        """

        :return: generate a random array (length and range of value were defined in init)
        """
        if self.n == 0:
            self.n = random.randrange(self.range)
        for i in range(self.n):
            self.array.append(random.randrange(self.range))
        return self.array

    def selection_sort(self):
        """
        reference: https://www.geeksforgeeks.org/selection-sort/
        find the least minimum value and swap it with the first index of array
        find the next least minimum value and swap it with second index of array.
        do it until array was sorted
        :return: sorted array
        """
        n = len(self.array)
        start = self.get_timer()
        for i in range(n):
            sleep(0.1)
            # get the current index,
            cur_ind = i
            for j in range(i+1, n):
                # find the minimum value in an array, from current index
                if self.array[cur_ind] > self.array[j]:
                    cur_ind = j
            # if index of the minimum value is current index, then swap it
            if cur_ind != i:
                tmp = self.array[i]
                self.array[i] = self.array[cur_ind]
                self.array[cur_ind] = tmp
        stop = self.get_timer()
        self.time = stop - start
        return self.array

    def bubble_sort(self):
        """
        reference: https://www.geeksforgeeks.org/bubble-sort/
        step 1: compare first two element, and swap if second is less then first
        do it until comparing whole array.
        step 2: repeat step 1 with compared array which was in step 1
        Note: this algorithm need run step 1 one more time to confirm that the array were sorted
        :return: sorted array
        """
        n = len(self.array)
        # this is a variable which confirm the array were sorted, because of no swap
        con = 1
        start = self.get_timer()
        # print(start)
        while con == 1:
            sleep(1)
            con = 0
            # step 1: compare whole elements in array
            for i in range(n-1):
                # swap if the current element is more than next one
                if self.array[i] > self.array[i+1]:
                    tmp = self.array[i]
                    self.array[i] = self.array[i+1]
                    self.array[i+1] = tmp
                    # this variable is set to 1 , if swap element
                    con = 1
        stop = self.get_timer()
        self.time = stop - start
        return self.array

    def recursive_bubble_sort(self):
        """
        reference: https://www.geeksforgeeks.org/recursive-bubble-sort/
        step 1: compare first two element, and swap if second is less then first
        do it until comparing whole array.
        step 2: repeat step 1 with compared array which was in step 1
        Note: this algorithm need run step 1 one more time to confirm that the array were sorted
        :return: sorted array
        """
        n = len(self.array)
        # this is a variable which confirm the array were sorted, because of no swap
        con = 0
        start = self.get_timer()
        # print(start)
        sleep(0.5)
        # step 1: compare whole elements in array
        for i in range(n-1):
            sleep(0.1)
            # swap if the current element is more than next one
            if self.array[i] > self.array[i+1]:
                tmp = self.array[i]
                self.array[i] = self.array[i+1]
                self.array[i+1] = tmp
                # this variable is set to 1 , if swap element
                con = 1
        # if the array was not sorted, then call recursive_bubble_sort
        if con == 1:
            self.recursive_bubble_sort()
        stop = self.get_timer()
        # print(stop)
        self.time = stop - start
        return self.array


class Graphic:
    white = (255, 255, 255)
    red = (255, 0, 0)

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.dis = None
        self.con = False
        self.arr = []

    def init_display(self):
        self.dis = pygame.display.set_mode((self.w, self.h))

    def draw_array(self, array, color):
        for i in range(len(array)):
            rect = ((i * 2, 10), (1, array[i] * 4))
            pygame.draw.rect(self.dis, color, rect)

    def run(self, color, array, con):
        while con:
            self.dis.fill(color)
            self.draw_array(array, self.red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    quit()


sort_al = SortAlgorithm(40, 80)
ar = sort_al.random_array()
print(ar)
# print(sort_al.bubble_sort())
gra = Graphic(320, 320)
gra.init_display()
t1 = Thread(target=sort_al.recursive_bubble_sort)
t1.start()
gra.run(gra.white, sort_al.array, True)
t1.join()
print('DOne')
