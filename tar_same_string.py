'''
@describle: 链接：https://www.nowcoder.com/questionTerminal/8e5d1e50cea94d438fbc842063d44cd1?orderByHotValue=1&mutiTagIds=239_645&page=1&onlyReference=false
来源：牛客网

通过键盘输入一串小写字母(a~z)组成的字符串。请编写一个字符串压缩程序，将字符串中连续出席的重复字母进行压缩，并输出压缩后的字符串。
压缩规则：
1、仅压缩连续重复出现的字符。比如字符串"abcbc"由于无连续重复字符，压缩后的字符串还是"abcbc"。
2、压缩字段的格式为"字符重复的次数+字符"。例如：字符串"xxxyyyyyyz"压缩后就成为"3x6yz"。
要求实现函数：
void stringZip(const char *pInputStr, long lInputLen, char *pOutputStr);
【输入】
pInputStr：  输入字符串
lInputLen：  输入字符串长度
【输出】 pOutputStr： 输出字符串，空间已经开辟好，与输入字符串等长；
【注意】只需要完成该函数功能算法，中间不需要有任何IO的输入输出
示例
输入：“cccddecc”   输出：“3c2de2c”
输入：“adef”     输出：“adef”
输入：“pppppppp” 输出：“8p”
@datatime: 20200402
'''


def tar_same_str(data_strings):
    lens = len(data_strings)
    data_strings_list = list(data_strings)
    temp_arr = []
    result_arr = []
    for index in range(lens):
        temp_arr.append(data_strings_list[index])
        if temp_arr[0] != data_strings_list[index]:
            if len(temp_arr) > 2:
                result_arr.append(str(len(temp_arr)-1))
            result_arr.append(temp_arr[0])
            temp_arr = []
            temp_arr.append(data_strings_list[index])
            if index == lens -1:
                result_arr.append(data_strings_list[index])
        elif index == lens -1:
            result_arr.append(str(len(temp_arr)))
            result_arr.append(data_strings_list[index])
    return ''.join(result_arr)


print(tar_same_str('aaafffffdseee'))