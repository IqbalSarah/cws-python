def removeDuplicates(my_list: list[int]):
    list1 = []
    for i in my_list:
        if i not in list1:
            list1.append(i)
    return list1


print(removeDuplicates(my_list=[1, 2, 3, 4, 4, 6, 6, 5]))
