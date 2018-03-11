number_list = [-1, 1, 2, 5, 7, 8657, 2, 99997, 431, 3, 432, 4325]


def find_max(list):
    largest = list[0]
    for i in list:
        temp = largest
        # print ("temp is :", temp)
        if temp < i:
            largest = i
        elif temp == i:
            largest = i
        else:
            largest = temp
    print ('larget number is :', largest)


def find_min(list):
    smallest = None
    for i in list:
        temp = smallest
        if smallest is None:
            smallest = i
        elif temp < i:
            smallest = temp
        else:
            smallest = i
    print ('the smallest number is :', smallest)


print(find_min(number_list))
