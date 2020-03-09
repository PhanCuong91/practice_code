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
        self.pivot = 0

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
                # sleep(0.1)
                if self.array[i] > self.array[j]:
                    arr_tmp.pop(j-l)
                    arr_tmp.insert(i-l+move, self.array[j])
                    move += 1
                    j += 1
                else:
                    i += 1
            # assign to array
            self.array[l:r] = arr_tmp
            # sleep(0.2)
        stop = self.get_timer()
        self.time = stop - start

    def quick_sort(self, arr, l, r):
        n = len(arr)
        if len(arr) > 1:
            pivot = arr[n-1]
            # print('pivot %d n is %d' % (pivot, n-1))
            small = []
            n_small = 0
            big = []
            n_big = 0
            # print("function array")
            # print(arr)
            for i in range(n-1):
                if arr[i] <= pivot:
                    n_small += 1
                    small.append(arr[i])
                else:
                    n_big += 1
                    big.append(arr[i])

            # print("z is %d \n" % z)
            # print(str(pivot) + '\n')

            if len(small) != 0:
                self.array[l: l+n_small] = small
            self.array[l+n_small] = pivot
            self.pivot = l+n_small
            print('function %d' % self.pivot)
            if len(big) != 0:
                self.array[r-n_big: r] = big
            sleep(0.5)
            # print("main array")
            # print(self.array)
            if len(small) > 1:
                # self.small += 1
                # print("small: %d big  %d" % (self.small, self.big))
                # print(small)

                # print("left is %d and right %d and n small = %d" % (l,r, n_small))
                # print(small)
                small = self.quick_sort(small, l, l+n_small)

            if len(big) > 1:
                # self.big += 1
                # print("big: %d, small %d" % (self.big, self.small))
                # print(big)

                # print("n big = %d and and left %d and right is %d" % (n_big,l, r))
                # print(big)
                big = self.quick_sort(big, r - n_big, r)
            # sleep(0.2)

            return arr
        else:
            return []


class Graphic:
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

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

    def run(self, color, array, pivot):
        tmp = 0
        while True:
            self.dis.fill(color)
            self.draw_array(array, self.red)
            if tmp != pivot:
                print(pivot)
            tmp = pivot
            rect = ((pivot * 2, 10), (1, array[pivot] * 4))
            pygame.draw.rect(self.dis, self.blue, rect)
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
af = sort_al.insertion_sort()
print(af)
print(sort_al1.array)
print(sort_al1.array.count(91))
# ar1 = sort_al1.quick_sort(sort_al1.array)
# print(ar1)
# print(ar1.count(91))
# print(sort_al1.time)
# print(sort_al.array)
# print(sort_al1.array)

gra = Graphic(500, 500)
gra.init_display()
t1 = Thread(target=sort_al1.quick_sort, args=(sort_al1.array, 0, 100))
t1.start()
gra.run(gra.white, sort_al1.array, sort_al1.pivot)
# print(sort_al1.array)
t1.join()
# print(sort_al1.array)


print('DOne')
