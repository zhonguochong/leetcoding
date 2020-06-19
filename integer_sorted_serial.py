'''
链接：https://www.nowcoder.com/questionTerminal/7f22090b683149f082bd1f48565e4b20?mutiTagIds=239_645&orderByHotValue=1
来源：牛客网

输入一组大于等于0的整数，根据从大到小的顺序排序后输出；如果排序后有连续数时，只输出连续输的最大和最小数。输入的所有整数都各不相同，即不用考虑两个整数相同的情况。
如： 输入4,7,2,1,5,8,9,11 输出11,9,7,5,4,2,1
@author: kuochung
@email: jxgxzgc@163.com
@datetime: 20200403
'''


def inter_sort_serial(*nums):
    nums_sorted = sorted(nums, reverse=True)
    temp_arr = [nums_sorted[0]]
    result_arr = []
    for item in nums_sorted[1:]:
        if temp_arr[-1] - item == 1:
            if item == nums_sorted[-1]:
                result_arr.append(temp_arr[0])
                result_arr.append(item)
            else:
                temp_arr.append(item)
        else:
            result_arr.append(temp_arr[0])
            if len(temp_arr) > 1:
                result_arr.append(temp_arr[-1])
            if item == nums_sorted[-1]:
                result_arr.append(item)
            temp_arr = [item]
    return result_arr


if __name__ == '__main__':
    print(inter_sort_serial(4, 7, 2, 1, 5, 8, 9, 11))
    print(inter_sort_serial(3, 8, 23, 4, 2, 0, 5, 10))
