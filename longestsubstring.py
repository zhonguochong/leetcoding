# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         tmp = []
#         length = 0
#         length_tmp = 0
#         index = 0
#         for i in s:
#             if i  not in tmp:
#                 tmp.append(i)
#                 length = length + 1
#             else:
#                 index = tmp.index(i)
#                 del tmp[:index+1]
#                 tmp.append(i)
#                 length = len(tmp)
#             if length_tmp < length:
#                 length_tmp =  length
#         return length_tmp

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str=""
        str_ = ""
        for i in s:
            if i not in str_:
                str_+= i
            else:
                if len(max_str)<len(str_):
                    max_str=str_              
                str_=str_[str_.index(i)+1:]+i
        if len(max_str)<len(str_):
            max_str=str_
        return len(max_str)

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(" "))