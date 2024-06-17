def merge_two_sorted_lists(l1, l2):
    l1 = [5,4,23,45,12,9,49,1,3]
    l2 = [2,32,44,7,8,4,11]
    sum_list = l1 + l2
    sorted_list = sorted(sum_list)
    print(sorted_list)

l1 = [5, 4, 23, 45, 12, 9, 49, 1, 3]
l2 = [2, 32, 44, 7, 8, 4, 11]
merge_two_sorted_lists(l1,l2)
