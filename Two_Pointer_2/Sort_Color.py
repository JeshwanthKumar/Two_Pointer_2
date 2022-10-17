#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero = 0    #Intialize zero pointer to 0
        first = 0   #Initialize first pointer to 0
        second = len(nums)-1    #Initialize second pointer to last index which is len(nums)-1
        
        for i in range(len(nums)):  #Continue for the length of nums
            
            if nums[first] == 1:    #If nums[first] is 1 then increment first by 1
                first += 1
                
            elif nums[first] == 0:  #Else if nums[first] is 0 swap nums[first] and nums[zero]
                nums[zero], nums[first] = nums[first], nums[zero]
                zero += 1   #Increment zero by 1
                first += 1  #Increment first by 1
                
                
            else:   #Else swap nums[first] and nums[second] which mean the nums[i] is 2
                nums[first], nums[second] = nums[second], nums[first]
                second -= 1 #Decrement secind by 1