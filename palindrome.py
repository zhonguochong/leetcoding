class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0 or (x % 10 ==0 and x != 0) :
        #     return False
        # x = str(x)
        # for i in range(len(x)//2):
        #     if x[i] != x[-i -1]:
        #         return False
        # return True

        # if x < 0 or (x % 10 ==0 and x != 0) :
        #     return False
        # tmp = 0
        # while(x > tmp):
        #     tmp = tmp * 10 + x % 10
        #     x //= 10
        # return x == tmp or x == tmp // 10
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(123))
    print(s.isPalindrome(-123))
    print(s.isPalindrome(10))