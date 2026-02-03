class Solution:
    def isPalindrome(self, n):
		# code heren
		x=n
		rev=0
		while x!=0:
		    l=x%10
		    rev=rev*10+l
		    x=x//10
		if rev==n:
		    return True
		else:
		    return False
		   