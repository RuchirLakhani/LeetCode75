class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeroes = 0
        fullproduct = 1
        output = []
        for idx,number in enumerate(nums):
            
            if number == 0:
                zeroes += 1
                position  = idx
            
                if zeroes > 1:
                    return [0]*len(nums)
            else:
                fullproduct *= number 
        
        if zeroes:
            output = [0]*len(nums)
            output[position] = fullproduct
            return output
        else:
            return [fullproduct//i for i in nums]