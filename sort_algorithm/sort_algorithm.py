import random
import timeit

class SortAlgorithm:
    def __init__(self, n=None, range=100):
        self.n = n
        self.range = range
        self.array = []
        self.time = 0

    def get_timer(self):
        return timeit.default_timer()

    def random_array(self):
        array = []
        if self.n == None:
            self.n = random.randrange(self.range)
        for i in range(self.n):
            self.array.append(random.randrange(self.range))
        return self.array

    def selection_sort(self):
        n = len(self.array)
        start = self.get_timer()
        print(start)
        for i in range(n):
            m = i
            for j in range(i+1, n):
                if self.array[m] > self.array[j]:
                    m = j
            if m != i:
                tmp = self.array[i]
                self.array[i] = self.array[m]
                self.array[m] = tmp
        stop = self.get_timer()
        print(stop)
        self.time = stop - start
        return self.array


print(timeit.default_timer())
sort_al = SortAlgorithm(10000, 10000)
ar = sort_al.random_array()
print(timeit.default_timer())
print(ar)
print(sort_al.selection_sort())
print(sort_al.time)
