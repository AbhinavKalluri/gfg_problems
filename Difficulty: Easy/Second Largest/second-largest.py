class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest=arr[0]
        sec_lar=-1
        for x in arr:
            if x>largest:
                largest=x
        for y in arr:
            if y>sec_lar and y!=largest:
                sec_lar=y
        return sec_lar
        