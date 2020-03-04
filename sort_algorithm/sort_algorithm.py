import random
import timeit
from graphic import Graphic


class SortAlgorithm(Graphic):
    def __init__(self, n=None, range=100):
        self.n = n
        self.range = range
        self.array = []
        Graphic.__init__(self,320,320)
        Graphic.init_display(self)

    def get_timer(self):
        return timeit.default_timer()

    def random_array(self):
        if self.n == None:
            self.n = random.randrange(self.range)
        for i in range(self.n):
            self.array.append(random.randrange(self.range))
        return self.array

    def selection_sort(self):
        n = len(self.array)
        start = self.get_timer()
        # print(start)
        for i in range(n):
            m = i
            for j in range(i+1, n):
                if self.array[m] > self.array[j]:
                    m = j
            if m != i:
                tmp = self.array[i]
                self.array[i] = self.array[m]
                self.array[m] = tmp
            Graphic.run(self, self.white, self.array, False)
        stop = self.get_timer()
        # print(stop)
        self.time = stop - start
        return self.array

    def bubble_sort(self):
        n = len(self.array)
        con = 1
        start = self.get_timer()
        # print(start)
        while con != 1:
            con = 0
            for i in range(n-1):
                if self.array[i] > self.array[i+1]:
                    tmp = self.array[i]
                    self.array[i] = self.array[i+1]
                    self.array[i+1] = tmp
                    con = 1
        stop = self.get_timer()
        # print(stop)
        self.time = stop - start
        return self.array

    def recursive_bubble_sort(self):
        n = len(self.array)
        con = 1
        start = self.get_timer()
        # print(start)
        while con != 1:
            con = 0
            for i in range(n-1):
                if self.array[i] > self.array[i+1]:
                    tmp = self.array[i]
                    self.array[i] = self.array[i+1]
                    self.array[i+1] = tmp
                    con = 1
        stop = self.get_timer()
        # print(stop)
        self.time = stop - start
        return self.array

    
# print(timeit.default_timer())
sort_al = SortAlgorithm(10000, 600)
ar = sort_al.random_array()
# print(timeit.default_timer())
print(ar)
print(sort_al.selection_sort())
sort_al.run(sort_al.white,sort_al.array, True)
# print(sort_al.time)
# print(sort_al.bubble_sort())
# print(sort_al.time)
