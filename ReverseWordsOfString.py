class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_list = s.split()
        output = ""
        i = len(s_list) - 1
        while i >= 0:
            
            output += s_list[i]
 
            if i != 0:
                output += " "  

            i -= 1

        return output