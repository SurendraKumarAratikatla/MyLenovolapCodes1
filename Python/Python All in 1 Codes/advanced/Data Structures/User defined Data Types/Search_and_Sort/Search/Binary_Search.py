from time_cal import time_taken

@time_taken
def linear_search(numbers_list, number_to_find):
    for index, number in enumerate(numbers_list):
        if number == number_to_find:
            return index
    return -1

@time_taken
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_number
        elif mid_number <= number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


numbers_list = [i for i in range(1000001)]
number_to_find = 1000000
li_indx = linear_search(numbers_list, number_to_find)
bi_indx = binary_search(numbers_list, number_to_find)
print("Linear search finding number index is : " + str(li_indx))
print("Binary search finding number index is : " + str(bi_indx))