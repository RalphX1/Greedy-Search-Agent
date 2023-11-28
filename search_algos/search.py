#Example: Floating point division 
print(5 / 2)  # Output: 2.5
#Example: Integer (floor) division
print(5 // 2) # Output: 2 

n = [1,2,3,4,5,6,7,8,9,10]

# Linear Search 
#look for number 6
print("Startig linear search.")
print("--------------------------")
linlook = 6
for i in n:
    if (i != linlook):
        print("This is not number 6!")
    elif (i == linlook):
        print("I found number", linlook, "at position", n[5], "!!!")
        break
print("--------------------------")
print("End of linear search.")
#-----------------------------------------------------------------------------------------------
# Binary Search 
#look for number 8
print("Startig binary search.")
print("--------------------------")
high = len(n) - 1
print("Initiate high with = ", high)
low = 0
print("Initiate low with = ", low)
bintarget = 9
middle_index = (low + high) // 2 #4
print("Initiate middle_index with = ", middle_index)
middle_value = n[middle_index] #5
print("Initiate middle_value with = ", middle_value)
while low <= high and middle_value != bintarget:
    if middle_value > bintarget:
        high = middle_index - 1
        print("High is now = ", high)
    elif middle_value < bintarget:
        low = middle_index + 1
        print("Low is now = ", low)
    middle_index = (low + high) // 2
    print("middle_index is now = ", middle_index)
    middle_value = n[middle_index] 
    print("middle_value is now = ", middle_value)   

if middle_value == bintarget:
    print("I found number", bintarget, "at position", n[middle_index], "!!!")
else: 
    print(bintarget, "not found in list")
print("--------------------------")
print("End of binary search.")
#-----------------------------------------------------------------------------------------------

