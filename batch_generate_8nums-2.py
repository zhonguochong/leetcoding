'''
@Author: your name
@Date: 2020-06-24 9:02:41
@LastEditTime: 2020-06-24 11:09:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
2. 打开微信，设置-->账号与安全-->声音锁-->开始。屏幕中会出现一个八位数字。观察数字
规律（可多次点击开始），请用代码批量实现有同样规律的数字。(0不能在第一位，每一位数字不重复，范围是0-9)
@FilePath: /leetcoding/batch_generate_8nums.py
'''
import random

def batch_generate_8nums(counts):
    while counts:
        first_unit = random.randint(1, 9)  # 第一位数的范围是【1，9】
        # 剩下七位数的范围是【0，9】除去第一位生成的数
        rest_units = [item for item in range(10)]
        rest_units.remove(first_unit)
        # 从中采样7个数并随机洗牌
        rest_units = random.sample(rest_units, 7)
        random.shuffle(rest_units, random = None)
        
        print(eval(str(first_unit) + ''.join([str(item) for item in rest_units] )))
        counts -= 1


if __name__ == '__main__':
    # 批量生成有同样规律的8位数
    batch_generate_8nums(10)
