def get_largest(nums):
   largest = nums[0]
   for num in nums:
       if num > largest:
           largest = num
   return largest
 
my_nums = [10,159,698,100,0,-55]
 
largest = get_largest(my_nums)
 
print('The largest number is: ', largest)