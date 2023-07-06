class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left , right = 0 , len(s) - 1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        output=""
        s_list = list(s)
        while left < right:
            
            if s_list[left] in vowels and s_list[right] in vowels:
                temp = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = temp
                left += 1
                right -= 1

            elif s_list[left] in vowels and s_list[right] not in vowels:
                right -= 1
            
            elif s_list[left] not in vowels and s_list[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
                
        return "".join(s_list)


