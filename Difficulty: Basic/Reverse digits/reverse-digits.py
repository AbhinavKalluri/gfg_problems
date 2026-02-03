#User function Template for python3

class Solution:
	def reverseDigits(self, n):
	    rev=0
	    while n!=0:
	        l=n%10
	        if l!=0:
	            rev=rev*10+l
	        n=n//10
	    return rev
		# Code here