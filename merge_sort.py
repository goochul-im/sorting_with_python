def merge_sort(lst: list, left: int, right: int):
    center = (left + right) // 2

    if left < right:
        merge_sort(lst, left, center)
        merge_sort(lst, center + 1, right)

        left_point, right_point, buff_point = left, right, left
        buff = lst[:]

        while left_point <= center and right_point <= right:
            if lst[left_point] <= lst[right_point]:
                buff[buff_point] = lst[left_point]
                left_point += 1
            else:
                buff[buff_point] = lst[right_point]
                right_point += 1
            buff_point += 1

        while left_point <= center:
            buff[buff_point] = lst[left_point]
            left_point += 1
            buff_point += 1
        while right_point <= right:
            buff[buff_point] = lst[right_point]
            right_point += 1
            buff_point += 1

        lst[left:right + 1] = buff[left:right + 1]


temp_list = [10, 2, 7, 9, 15, 1, 4, 5, 8]
merge_sort(temp_list,0,len(temp_list) - 1)
print(temp_list)
