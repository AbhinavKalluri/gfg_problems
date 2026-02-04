class Solution:
    def largest(self, arr):
        # code here
        lar=arr[0]
        for x in arr:
            if x>lar:
                lar=x
        return lar