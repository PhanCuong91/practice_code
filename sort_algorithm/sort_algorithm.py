import random
import timeit
from threading import Thread
from time import sleep
import pygame


class SortAlgorithm:
    def __init__(self, n=0, rag=100):
        """
        :param self.n: number of array
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
        self.n = len(self.array)
        start = self.get_timer()
        for i in range(self.n):
            sleep(0.1)
            # get the current index,
            cur_ind = i
            for j in range(i+1, self.n):
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
        self.n = len(self.array)
        # this is a variable which confirm the array were sorted, because of no swap
        con = 1
        start = self.get_timer()
        # print(start)
        while con == 1:
            sleep(1)
            con = 0
            # step 1: compare whole elements in array
            for i in range(self.n-1):
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

    def recursive_bubble_sort(self, n):
        """
        reference: https://www.geeksforgeeks.org/recursive-bubble-sort/
        step 1: compare first two element, and swap if second is less then first
        do it until comparing whole array.
        step 2: repeat step 1 with compared array which was in step 1
        Note: this algorithm need run step 1 one more time to confirm that the array were sorted
        :return: sorted array
        """

        start = self.get_timer()
        if n == 1:
            return self.array
        for i in range(n-1):
            # swap if the current element is more than next one
            # next one will be current
            if self.array[i] > self.array[i+1]:
                tmp = self.array[i]
                self.array[i] = self.array[i+1]
                self.array[i+1] = tmp
        # after swapping, the largest element shall be at the end of array
        self.recursive_bubble_sort(n-1)
        stop = self.get_timer()
        self.time = stop - start

    def insertion_sort(self):
        """
        reference: https://www.geeksforgeeks.org/insertion-sort/
        first element is a sorted array. then get and sort next element in the exiting sorted array.
        for example: sorted array: array[0]. then get array[1] and sort. after that, sorted array is array[0,1]
        :return:
        """
        for i in range(1, self.n):
            # sort the next element to the exiting sorted array
            for j in range(i):
                sleep(0.001)
                # sort element: get next element and find suitable index in exiting sorted array
                # then delete next element  and insert it to the above index
                if self.array[i] < self.array[j]:
                    tmp = self.array[i]
                    self.array.pop(i)
                    self.array.insert(j, tmp)
                    break
        return self.array

    def recursive_insertion_sort(self, n):
        """
        reference: https://www.geeksforgeeks.org/insertion-sort/
        first element is a sorted array. then get and sort next element in the exiting sorted array.
        for example: sorted array: array[0]. then get array[1] and sort. after that, sorted array is array[0,1]
        :return:
        """
        tmp = self.n - n + 1
        if tmp == self.n:
            return self.array
        for i in range(tmp):
            if self.array[i] > self.array[tmp]:
                temp = self.array[tmp]
                self.array.pop(tmp)
                self.array.insert(i, temp)
                break
        self.recursive_insertion_sort(n-1)


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
af = sort_al.recursive_insertion_sort(sort_al.n)
print(af)
print(sort_al.array)

# gra = Graphic(320, 320)
# gra.init_display()
# t1 = Thread(target=sort_al.recursive_insertion_sort)
# t1.start()
# print(sort_al.array)
# gra.run(gra.white, sort_al.array, True)
# t1.join()
print('DOne')
