from computer_time import timer
class Solution(object):
    @timer
    def twoSum(self, nums, target):
        """
        :type nums: List
        :type target: int
        """
        map_a = dict()
        for i in range(len(nums)):   #一边将列表中的数添加到字典中，一边判断两数之差是否存在于字典中
            temp = target - nums[i]  
            if temp in map_a :  # 判断步骤
                print( [map_a[temp], i])
                break
            map_a[nums[i]] =  i  # 添加步骤（切记先判断再添加，以免key冲突)
s = Solution()
s.twoSum([2, 7, 9, 11, 15], 9)