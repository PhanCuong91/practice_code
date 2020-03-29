from graphic import Graphic
from sort_algorithm import SortAlgorithm
from threading import Thread

sort_all = SortAlgorithm(64, 100)
sort_all.dict_arr['selection'] = sort_all.random_array()
sort_all.dict_arr['quick'] = sort_all.random_array()
sort_all.dict_arr['merge'] = sort_all.random_array()
sort_all.dict_arr['re_insertion'] = sort_all.random_array()
sort_all.dict_arr['insertion'] = sort_all.random_array()
sort_all.dict_arr['bubble'] = sort_all.random_array()
sort_all.dict_arr['heap'] = sort_all.random_array()
# sort_all.dict_arr['count'] = sort_all.random_array()
sort_all.dict_arr['bitonic'] = sort_all.random_array()
sort_all.bitonic_sort()
print(sort_all.dict_arr['count'])
sort_all.dict_arr['insertion'] = sort_all.dict_arr['bitonic']
# sort_all.count_sort()
print(sort_all.dict_arr['count'])
# sort_all.dict_arr['heap'] = [16, 28, 11, 94, 56]
# # print(sort_all.dict_arr['heap'])
# sort_all.heap_sort(5)
# print(sort_all.dict_arr['heap'])
# sort_all.dict_arr['heap'] = [16, 28, 56, 11, 94]
# # print(sort_all.dict_arr['heap'])
# sort_all.heap_sort(5)
# print(sort_all.dict_arr['heap'])

sort_all.sleep = 0.3
# t1 = Thread(target=sort_all.quick_sort, args=(0, 100,))
# t1 = Thread(target=sort_all.merge_sort, args=(0, 100,))
# t1 = Thread(target=sort_all.selection_sort)
# t1 = Thread(target=sort_all.bubble_sort)
# t1 = Thread(target=sort_all.insertion_sort)
# t1 = Thread(target=sort_all.heap_sort, args=(100,))
# t1.start()
gra = Graphic(1020, 500)
gra.init_display()

while True:
    # gra.run(gra.white, sort_all.dict_arr['quick'], 'quick', sort_all.dict_gra_infor)
    # gra.run(gra.white, sort_all.dict_arr['merge'], 'merge', sort_all.dict_gra_infor)
    # gra.run(gra.white, sort_all.dict_arr['selection'], 'selection', sort_all.dict_gra_infor)
    # gra.run(gra.white, sort_all.dict_arr['bubble'], 'bubble', sort_all.dict_gra_infor)
    gra.run(gra.white, sort_all.dict_arr['insertion'], 'insertion', sort_all.dict_gra_infor)
    # gra.run(gra.white, sort_all.dict_arr['heap'], 'heap', sort_all.dict_gra_infor)
t1.join()
print('DOne')
