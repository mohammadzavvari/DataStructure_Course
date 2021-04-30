def partition_v1(x, left, right):  # TODO: It has a bug.
    if left >= right:
        return
    pivot = x[right]
    pivot_index = right
    i = left
    j = right - 1
    swap_left = False
    swap_right = False
    while i <= j:
        if not swap_left and x[i] < pivot:
            i += 1
        else:
            swap_left = True
        if not swap_right and x[j] > pivot:
            j -= 1
        else:
            swap_right = True

        if swap_right and swap_left:
            x[i], x[j] = x[j], x[i]
            swap_right = swap_left = False

    if swap_left:
        x[i], x[pivot_index] = x[pivot_index], x[i]
        print(x)
        partition(x, left, i-1)
        partition(x, i, right)

    elif swap_right:
        x[j+1], x[pivot_index] = x[pivot_index], x[j+1]
        print(x)
        partition(x, left, j)
        partition(x, j+1, right)

    else:  # Now i = j. So, we have:
        if x[j] > pivot:
            x[j], x[pivot_index] = x[pivot_index], x[j]
            print(x)
            partition(x, left, j-1)
            partition(x, j, right)
        print(x)
        partition(x, left, pivot_index-1)
    return


def quick_sort_v1(x):
    partition_v1(x, 0, len(x))
    return x


def quick_sort(x, left, right):
    if right <= left:
        return
    pivot_index = partition(x, left, right)
    quick_sort(x, left, pivot_index-1)
    quick_sort(x, pivot_index+1, right)
    return


def partition(x, left, right):
    left_p = left
    right_p = right - 1
    pivot = x[right]
    pivot_index = right

    while left_p <= right_p:

        while x[left_p] <= pivot:  # Or we can use this: while left_p < right and x[left_p] <= pivot:
            if left_p >= right:
                break
            left_p += 1

        while x[right_p] > pivot:  # Or we can use this: while right_p >= left and x[right_p] > pivot:
            if right_p < left:
                break
            right_p -= 1

        if left_p < right_p:
            x[left_p], x[right_p] = x[right_p], x[left_p]

    x[left_p], x[pivot_index] = x[pivot_index], x[left_p]
    pivot_index_new = left_p
    return pivot_index_new


def partition_class(x, left, right):
    left_p = left
    right_p = right - 1
    pivot = x[right]
    pivot_index = right

    while left_p <= right_p:

        while left_p < right and x[left_p] <= pivot:
            left_p += 1

        while right_p >= left and x[right_p] > pivot:
            right_p -= 1

        if left_p < right_p:
            x[left_p], x[right_p] = x[right_p], x[left_p]

    x[left_p], x[pivot_index] = x[pivot_index], x[left_p]
    pivot_index_new = left_p
    return pivot_index_new
