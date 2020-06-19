class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        y = list(str(x))
        tmp = (len(y)+1)//2
        for i in range(tmp):
            a = y[i]
            y[i] = y[len(y)-i-1] 
            y[len(y)-i-1] = a
        if int(''.join(y)) > 2**31:
            return 0
        if flag:
            return ~int(''.join(y))+1
        else:
            return int(''.join(y))
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
    print(s.reverse(-123))
    print(s.reverse(123))
    print(s.reverse(2147483647))