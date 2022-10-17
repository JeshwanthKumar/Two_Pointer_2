#Time_Complexuty: O(n)
#SPace_Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1    #Initialize slow pointer to 1
        fast = 1    #Initialize fast pointer to 1
        count =1    #Initialize count to 1
        k = 2   #Initialize k to 2 
        n = len(nums)   #n is the lenght of nums
        for fast in range(1, n):    #Continu fast till the lenght of nums

            if nums[fast] == nums[fast-1]:  #If nums[fast] is equal to nums[fast-1] increment count by 1
                count+= 1   
            else:   #Else count will remain 1
                count = 1   
                
            if count <=k:   #If the count is equal to k then change nums[slow] to nums[fast]
                nums[slow] = nums[fast]
                slow+=1 #Increment slow by 1
        return slow #Return slow