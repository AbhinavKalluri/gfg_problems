#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        x=n
        res=0
        while n!=0:
            l=n%10
            res=res+(l**3)
            n=n//10
        if res==x:
            return True
        else:
            return False
            
            
            