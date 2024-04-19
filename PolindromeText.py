class Solution(object):
    def isPalindrome(self, s):

        clean_string = ''.join(c.lower() for c in s if c.isalnum())
        print(clean_string)
        
        if clean_string == clean_string[::-1]:
            return True
        else: 
            return False


s = "A man, a plan, a canal: Panama"
solution = Solution()
solution.isPalindrome(s)

