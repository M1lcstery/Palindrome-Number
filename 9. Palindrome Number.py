class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        string = "".join(reversed(str(x)))
        
        if string == str(x):
            return True
        else:
            return False
        
        
    isPalindrome(object, 121)