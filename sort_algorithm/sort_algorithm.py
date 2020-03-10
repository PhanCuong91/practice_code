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
        # quick has [pivot, [index of smaller element], [index of bigger element] ]
        self.quick = []
        self.sleep = 0


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
            sleep(self.sleep)
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
            sleep(self.sleep)
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
        start = self.get_timer()
        for i in range(1, self.n):
            # sort the next element to the exiting sorted array
            for j in range(i):
                # sleep(0.001)
                # sort element: get next element and find suitable index in exiting sorted array
                # then delete next element  and insert it to the above index
                if self.array[i] < self.array[j]:
                    tmp = self.array[i]
                    self.array.pop(i)
                    self.array.insert(j, tmp)
                    break
            sleep(self.sleep)
        stop = self.get_timer()
        self.time = stop - start
        return self.array

    def recursive_insertion_sort(self, n):
        """
        reference: https://www.geeksforgeeks.org/recursive-insertion-sort/
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

    def merge_sort(self, l, r):
        """

        :return:
        """
        # split array
        start = self.get_timer()
        if r - l > 1:
            m = int((r - l)/2)
            # sort first half of array
            self.merge_sort(l, l+m)
            # sort second half of array
            self.merge_sort(l+m, r)
            i = l
            j = l + m
            # save first or second half  to temporary array
            arr_tmp = self.array[l:r]
            move = 0
            # sort the half array
            # i is index of [41, 47], j  [1, 45]
            while i < l+m and j < r:
                # sleep(self.sleep)
                if self.array[i] > self.array[j]:
                    arr_tmp.pop(j-l)
                    arr_tmp.insert(i-l+move, self.array[j])
                    move += 1
                    j += 1
                else:
                    i += 1
            # assign to array
            self.array[l:r] = arr_tmp
            sleep(self.sleep)
        stop = self.get_timer()
        self.time = stop - start

    def quick_sort(self, left, right):
        self.quick = []
        n = right - left
        if n > 1:
            # get pivot at the end of array
            # pivot = arr[n-1]
            pivot = self.array[right-1]
            # create temp variable
            # array contains all elements which are less than pivot
            small = []
            # array contains all elements which are more than pivot
            big = []

            # search array[0:n-2]
            # if element is less than pivot, then save to small array
            # if element is more than pivot, then save to big array
            for i in range(left, right-1):
                if self.array[i] <= pivot:
                    # save to small array
                    small.append(self.array[i])
                else:
                    # save to big array
                    big.append(self.array[i])
            n_small = len(small)
            n_big = len(big)
            # replace main array with small and big array with respective to left and right parameters
            # assign small array to main array
            self.array[left: left+n_small] = small
            # assign pivot to main array
            self.array[left+n_small] = pivot
            # assign big array to main array
            self.array[right-n_big: right] = big

            # save information for graphic
            id_small = []
            id_big = []
            # get new pivot
            id_pivot = left+n_small
            self.quick.append(id_pivot)
            # get index of small and big array
            for i in range(left, left+n_small):
                id_small.append(i)
            self.quick.append(id_small)
            for i in range(right-n_big, right):
                id_big.append(i)
            self.quick.append(id_big)

            # print(self.array)
            sleep(self.sleep)

            # quick sort with new small and big arrays
            # do it until length of small and big arrays is 1
            self.quick_sort(left, left+n_small)
            self.quick_sort(right-n_big, right)
            return True
        else:
            return []


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

    def run(self, color, array, quick=[-1, [], []]):
        n = 0
        self.dis.fill(color)
        self.draw_array(array, self.red)

        # graphic for quick sort algorithm
        if len(quick) == 3:
            # print('quick')
            # print(quick)
            id_pivot = quick[0]
            id_small = quick[1]
            id_big = quick[2]
            # draw the pivot in display
            if id_pivot != -1:
                rect = ((id_pivot*self.distance, 10), (self.width_bar, array[id_pivot]*self.multi_height))
                pygame.draw.rect(self.dis, self.blue, rect)
            left = -1
            right = -1
            # draw small array in display
            if len(id_small) >= 1:
                for i in id_small:
                    rect = ((i*self.distance, 10), (self.width_bar, array[i]*4))
                    pygame.draw.rect(self.dis, self.green, rect)
                left = id_small[0]
                n = len(id_small)
            # draw big array in display
            if len(id_big) >= 1:
                for i in id_big:
                    rect = ((i*self.distance, 10), (self.width_bar, array[i]*self.multi_height))
                    pygame.draw.rect(self.dis, self.yellow, rect)
                right = id_big[len(id_big)-1]
                n = len(id_big)
            # draw working array which is running quick_sort()
            if left != -1 and right != -1:
                rect = ((left*self.distance, 0), ((right-left+1)*self.distance, 9))
                pygame.draw.rect(self.dis, self.purple, rect)
            elif left != -1:
                rect = ((left*self.distance, 0), (n*self.distance, 9))
                pygame.draw.rect(self.dis, self.purple, rect)
            elif right != -1:
                rect = (((right-n)*self.distance, 0), ((n+1)*self.distance, 9))
                pygame.draw.rect(self.dis, self.purple, rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()


sort_al = SortAlgorithm(100, 100)
sort_al1 = SortAlgorithm(100, 100)
ar = sort_al.random_array()
sort_al1.array = sort_al1.random_array()
# sort_al1.array = [20, 13, 81, 71, 15, 15, 13, 88, 30, 92]
# print(ar)
# af = sort_al.insertion_sort()
# print(af)
print(sort_al1.array)
print(sort_al1.array.count(91))
# ar1 = sort_al1.quick_sort(sort_al1.array)
# print(ar1)
# print(ar1.count(91))

gra = Graphic(1020, 500)
gra.init_display()
# t1 = Thread(target=sort_al1.merge_sort, args=(0, 40,))
sort_al1.sleep = 0.1
t1 = Thread(target=sort_al1.quick_sort, args=(0, 100,))
# t1 = Thread(target=sort_al1.merge_sort, args=(0, 100,))
t1.start()
while True:
    gra.run(gra.white, sort_al1.array, sort_al1.quick)
print(sort_al1.array)
t1.join()
print(sort_al1.array)


print('DOne')
