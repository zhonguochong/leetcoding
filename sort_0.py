'''
@describle: 链接：https://www.nowcoder.com/questionTerminal/116161f243b245db93aa1b0d32243d86?orderByHotValue=1&mutiTagIds=239_645&page=1&onlyReference=false
来源：牛客网

1.输入100以内的整数，以逗号离开； 2.将这些整数从大到小输出，中间以逗号隔开； 3.输出的数据中若含有三个以上的连续整数，则只输出连续列的最大值和最小值； 4.不考虑输入数字重复的情况。
例如:输入：1,2,3,4,7,8,9 输出：9,7,4,1
@datetime: 20200401
@author: jxgxzgc@163.com
'''


def sort_descend(list_num):
    sort_init = sorted(list_num, reverse=True)
    temp_array = []
    sort_result = []
    for item in sort_init:
        if temp_array != [] and temp_array[-1] - item > 1:
            sort_result.append(temp_array[0])
            if len(temp_array) > 1:
                sort_result.append(temp_array[-1])
            temp_array = []
        temp_array.append(item)
        if item == sort_init[-1]:
            sort_result.append(temp_array[0])
            if len(temp_array) > 1:
                sort_result.append(temp_array[-1])
    return sort_result


print(sort_descend([1, 2, 3, 4, 7, 8, 9]))
print(sort_descend([1, 2, 4, 5, 7]))
