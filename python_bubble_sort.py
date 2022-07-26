# This program is to perform the bubble Sort algorithm


# create and initialize array 
array = [10, 15, 25, 5, 75, 65, 100, 45]
# print unsorted array 
print(array)

# Loop through array moving smaller items to front, larger items to back of array to sort 
# Two loops:
# Outer loop goes through the entire array
# Inner loop will loop through start of array to (end of array - outer loop counter)
for out_loop_counter in range(0, len(array)-1):
    for in_loop_counter in range(0, (len(array) - 1 - out_loop_counter)):
        #if current index > next index SWAP
        if array[in_loop_counter] > array[in_loop_counter+1]:
            temp = array[in_loop_counter+1]
            array[in_loop_counter+1] = array[in_loop_counter]
            array[in_loop_counter] = temp

# print sorted array 
print(array)
