'''
@Author: your name
@Date: 2020-06-17 17:29:00
@LastEditTime: 2020-06-17 17:29:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /studyleetcode/sorted_ballute.py
'''
import sys
import random


class CheckOutException(Exception):
    def __init__(self):
        pass

class SortedBullute():
    def __init__(self):
        self.lis = []
        self.dic = {}
        self.choosed_pool = []
        self.result = []
        print('please input color and num of bullute each other:')
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break
                self.dic[line.split()[0]] = int(line.split()[-1].strip('\n'))
                self.choosed_pool.append(line.split()[0])
            if max([num for num in self.dic.values()]) <= (sum([num for num in self.dic.values()]) + 1) // 2:
                raise CheckOutError()
        except CheckOutException as result:
            print('CheckOutError: can not arrange from input data')
    def __call__(self):
        '''
        input: dic(key=color, value=num)
        output: sorted result
        ''' 
        tmp = None
        while max(self.dic.values()) > 0:
            choosed_color = random.choice(self.choosed_pool)
            if choosed_color ==  tmp:
                continue
            tmp = choosed_color
            self.result.append(tmp)
            self.dic[tmp] -= 1
            if self.dic[tmp] == 0:
                self.choosed_pool.remove(tmp)
        return self.result

            
if __name__ == "__main__":
    sb = SortedBullute()
    print(sb())