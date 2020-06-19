from computer_time import timer
class Solution():
    def __init__(self):
        self.list2 = []
        self.flag = False
    @timer
    def addTwoNumbers(self, list0, list1):
        for i in range(len(list0)):
            self.list2.append(list0[i] + list1[i])
        for j in range(len(self.list2)):
            if self.flag:
                self.list2[j] = self.list2[j] + 1
            if self.list2[j] // 10 != 0:
                self.list2[j] = self.list2[j] % 10
                self.flag = True
            else:
                self.flag = False
        print(self.list2) 

s = Solution()
s.addTwoNumbers([2,4,3],[5,6,4])