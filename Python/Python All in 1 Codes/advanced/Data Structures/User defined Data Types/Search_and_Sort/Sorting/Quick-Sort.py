# making partitions like in this array placing pivot element i.e. 11 at middle

def swap(a,b,arr):
    if a != b:
        temp =  arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements,start, end):
    pivot_index = start
    pivot_ele = elements[pivot_index]

    while start <= end:
        while start < len(elements) and elements[start] <= pivot_ele:
            start += 1

        while elements[end] > pivot_ele:
            end -= 1

        if start < end:
            swap(start,end, elements)
    swap(pivot_index, end, elements)
    #print(end)
    return end # returning partition index i.e. pivot element 11 index


def quick_sort(elements,start,end):
    if start < end:
        pi = partition(elements,start, end)
        quick_sort(elements, start, pi-1) # left partition
        quick_sort(elements, pi + 1, end) # right partition

if __name__ == "__main__":
    elements = [11, 7, 29, 9, 2, 15, 28]
    quick_sort(elements,0, len(elements)-1)
    print(elements)