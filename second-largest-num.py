# Program to find second largest element in list
# Time Complexity : O(N)
# run cmd: python3 second-largest-num.py

class Solution:
    def secondLargest(self, l):
        mx=max(l[0],l[1]) 
        secondmx=min(l[0],l[1]) 
        n =len(l)
        for i in range(2,n): 
            if l[i]>mx: 
                secondmx=mx
                mx=l[i] 
            elif l[i]>secondmx and mx != l[i]: 
                secondmx=l[i]
        return secondmx
 
print("Second Largest number is :", Solution().secondLargest([12,412,11,42,10,1]))