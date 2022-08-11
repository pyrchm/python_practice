def merge_sort(array):
    
    # pick a middle point. right now just middle
    array_length = len(array)
    
    if array_length > 1:
        pivot = array_length//2
    
        left_side  = array[:pivot]
        right_side = array[pivot:]
    
        merge_sort(left_side)
        merge_sort(right_side)
        
        # sort into main array
        # i = left side index
        # j = right side index
        # k = main array index
        i = j = k = 0;
        
        while (i < len(left_side)) and (j < len(right_side)):
            if left_side[i] <= right_side[j]:
                array[k] = left_side[i]
                k = k+1
                i = i+1 
            else:
                array[k] = right_side[j]
                k = k+1 
                j = j+1 
                
        
        #if one side counter is done
        while i < len(left_side):
            array[k] = left_side[i]
            k = k+1
            i = i+1
            
        while j < len(right_side):
            array[k] = right_side[j]
            k = k+1
            j = j+1
            
            
new_array = [5,3,2,4,8,3,5,2,3,5]
print("Unsorted")
print(new_array)

merge_sort(new_array)
print("Sorted")
print(new_array)
