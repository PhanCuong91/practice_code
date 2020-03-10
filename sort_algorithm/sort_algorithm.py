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
        self.dict_arr = {'selection': [], 'bubble': [], 're_bubble': [],
                         're_insertion': [], 'insertion': [], 'merge': [], 'quick': []}
        self.time = 0
        """
        dictionary of sort algorithm
        - insertion:  [sorted_arr, index of inserted element while sorting in sorted array]
        - bubble has [left, right] of two next element
        - selection has [[array contains the minimum element after searching], index of minimum element while searching]
        - merge has [left index of working array wrt main array, middle index of working array wrt main array,
                          # right index of working array wrt main array ]
        - quick has [pivot, left index of working array wrt main array, right index of working array wrt main array ]
        """
        self.dict_sort = {'insertion_sort': [[], -1],
                          'bubble_sort': [-1, -1],
                          'selection_sort': [[], -1, -1],
                          'merge_sort': [-1, -1, -1],
                          'quick_sort': [-1, -1, -1]}
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
        array = []
        if self.n == 0:
            self.n = random.randrange(self.range)
        for i in range(self.n):
            array.append(random.randrange(self.range))
        return array

    def selection_sort(self):
        """
        reference: https://www.geeksforgeeks.org/selection-sort/
        find the least minimum value and swap it with the first index of array
        find the next least minimum value and swap it with second index of array.
        do it until array was sorted
        :return: sorted array
        """
        array = self.dict_arr['selection']
        self.n = len(array)
        start = self.get_timer()
        for i in range(self.n):
            sleep(self.sleep)
            # get the current index,
            cur_ind = i
            for j in range(i+1, self.n):
                self.dict_sort['selection_sort'] = [(array[0:i]), cur_ind, j]
                sleep(self.sleep)
                # find the minimum value in an array, from current index
                if array[cur_ind] > array[j]:
                    cur_ind = j
            # if index of the minimum value is current index, then swap it
            if cur_ind != i:
                tmp = array[i]
                array[i] = array[cur_ind]
                array[cur_ind] = tmp

        stop = self.get_timer()
        self.time = stop - start
        self.dict_arr['selection'] = array
        return array

    def bubble_sort(self):
        """
        reference: https://www.geeksforgeeks.org/bubble-sort/
        step 1: compare first two element, and swap if second is less then first
        do it until comparing whole array.
        step 2: repeat step 1 with compared array which was in step 1
        Note: this algorithm need run step 1 one more time to confirm that the array were sorted
        :return: sorted array
        """
        array = self.dict_arr['bubble']
        self.n = len(array)
        # this is a variable which confirm the array were sorted, because of no swap
        con = 1
        len_sorted = 1
        start = self.get_timer()
        # print(start)
        while con == 1:
            sleep(self.sleep)
            con = 0
            # step 1: compare whole elements in array
            for i in range(self.n-len_sorted):
                self.dict_sort['bubble_sort'] = [i, i+1]
                # swap if the current element is more than next one
                if array[i] > array[i+1]:
                    tmp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = tmp
                    # this variable is set to 1 , if swap element
                    con = 1
                sleep(self.sleep)
            len_sorted += 1
        stop = self.get_timer()
        self.time = stop - start
        return array

    def recursive_bubble_sort(self, n):
        """
        reference: https://www.geeksforgeeks.org/recursive-bubble-sort/
        step 1: compare first two element, and swap if second is less then first
        do it until comparing whole array.
        step 2: repeat step 1 with compared array which was in step 1
        Note: this algorithm need run step 1 one more time to confirm that the array were sorted
        :return: sorted array
        """
        array = self.dict_arr['re_bubble']
        start = self.get_timer()
        if n == 1:
            return array
        for i in range(n-1):
            # swap if the current element is more than next one
            # next one will be current
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
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
        array = self.dict_arr['insertion']
        start = self.get_timer()
        for i in range(1, self.n):
            # sort the next element to the exiting sorted array
            for j in range(i):
                self.dict_sort['insertion_sort'] = [array[0:i], j]
                # sort element: get next element and find suitable index in exiting sorted array
                # then delete next element  and insert it to the above index
                if array[i] < array[j]:
                    tmp = array[i]
                    array.pop(i)
                    array.insert(j, tmp)
                    break
            sleep(self.sleep)
        stop = self.get_timer()
        self.time = stop - start
        return array

    def recursive_insertion_sort(self, n):
        """
        reference: https://www.geeksforgeeks.org/recursive-insertion-sort/
        first element is a sorted array. then get and sort next element in the exiting sorted array.
        for example: sorted array: array[0]. then get array[1] and sort. after that, sorted array is array[0,1]
        :return:
        """
        array = self.dict_arr['re_insertion']
        tmp = self.n - n + 1
        if tmp == self.n:
            return array
        for i in range(tmp):
            if array[i] > array[tmp]:
                temp = array[tmp]
                array.pop(tmp)
                array.insert(i, temp)
                break
        self.recursive_insertion_sort(n-1)

    def merge_sort(self, left, right):
        """

        :param left:
        :param right:
        :return:
        """
        self.merge = []
        # split array
        start = self.get_timer()
        if right - left > 1:
            m = int((right - left)/2)
            # run merge_sort for first half of array
            self.merge_sort(left, left+m)
            # run merge_sort for second half of array
            self.merge_sort(left+m, right)
            # after run merge_sort, first and second shall be sorted
            # sort the first or second half of array
            i = left
            j = left + m
            tmp = []
            # sort the half array
            while i < left+m and j < right:
                # sleep(self.sleep)
                if self.dict_arr['merge'][i] > self.dict_arr['merge'][j]:
                    tmp.append(self.dict_arr['merge'][j])
                    j += 1
                else:
                    tmp.append(self.dict_arr['merge'][i])
                    i += 1
            while i < left+m:
                tmp.append(self.dict_arr['merge'][i])
                i += 1
            while j < right:
                tmp.append(self.dict_arr['merge'][j])
                j += 1
            self.dict_sort['merge_sort'] = [left, m, right]
            sleep(self.sleep/2)
            # assign to array
            self.dict_arr['merge'][left:right] = tmp
            sleep(self.sleep/2)
        stop = self.get_timer()
        self.time = stop - start

    def quick_sort(self, left, right):
        """

        :param left:
        :param right:
        :return:
        """
        n = right - left
        if n > 1:
            # get pivot at the end of array

            pivot = self.dict_arr['quick'][right-1]
            # create temp variable
            # array contains all elements which are less than pivot
            small = []
            # array contains all elements which are more than pivot
            big = []

            # search array[0:n-2]
            # if element is less than pivot, then save to small array
            # if element is more than pivot, then save to big array
            for i in range(left, right-1):
                if self.dict_arr['quick'][i] <= pivot:
                    # save to small self.dict_arr['quick']
                    small.append(self.dict_arr['quick'][i])
                else:
                    # save to big array
                    big.append(self.dict_arr['quick'][i])
            n_small = len(small)
            n_big = len(big)
            # replace main array with small and big array with respective to left and right parameters
            # assign small array to main array
            self.dict_arr['quick'][left: left+n_small] = small
            # assign pivot to main array
            self.dict_arr['quick'][left+n_small] = pivot
            # assign big array to main array
            self.dict_arr['quick'][right-n_big: right] = big

            # save information for graphic
            self.dict_sort['quick_sort'] = [left+n_small, left, right]
            # end

            # print(array)
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
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()


sort_al1 = SortAlgorithm(100, 100)
sort_al1.dict_arr['selection'] = sort_al1.random_array()
sort_al1.dict_arr['quick'] = sort_al1.random_array()
sort_al1.dict_arr['merge'] = sort_al1.random_array()
sort_al1.dict_arr['re_insertion'] = sort_al1.random_array()
sort_al1.dict_arr['insertion'] = sort_al1.random_array()
sort_al1.dict_arr['bubble'] = sort_al1.random_array()
# sort_al1.array = [20, 13, 81, 71, 15, 15, 13, 88, 30, 92]


gra = Graphic(1020, 500)
gra.init_display()
sort_al1.sleep = 0.0
# t1 = Thread(target=sort_al1.quick_sort, args=(0, 100,))
# t1 = Thread(target=sort_al1.merge_sort, args=(0, 100,))
# t1 = Thread(target=sort_al1.selection_sort)
# t1 = Thread(target=sort_al1.bubble_sort)
t1 = Thread(target=sort_al1.insertion_sort)
t1.start()
while True:
    # gra.run(gra.white, sort_al1.dict_arr['quick'], 'quick_sort', sort_al1.dict_sort)
    # gra.run(gra.white, sort_al1.dict_arr['merge'], 'merge_sort', sort_al1.dict_sort)
    # gra.run(gra.white, sort_al1.dict_arr['selection'], 'selection_sort', sort_al1.dict_sort)
    # gra.run(gra.white, sort_al1.dict_arr['bubble'], 'bubble_sort', sort_al1.dict_sort)
    gra.run(gra.white, sort_al1.dict_arr['insertion'], 'insertion_sort', sort_al1.dict_sort)

t1.join()
print('DOne')
