class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #nums.sort()
        count = nums.count(0)
        nums[:] = [num for num in nums if num != 0 ]

        nums += [0] * count
