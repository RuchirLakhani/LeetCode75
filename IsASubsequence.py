class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        check = ""
        if s == t:
            return True

        while i < len(s) and j < len(t):

            if s[i] == t[j]:
                check += t[j]
                i += 1
                j += 1
                
            else:
                j += 1
        
        if check == s:
            return True
        return False

 
        