def quicksort(arr):

    def partition(array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]
        # pointer for greater element
        i = low -1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low,high):
            if array[j] <= pivot:

                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i+1

                # Swapping element at i with element at j
                (array[i],array[j]) = (array[j],array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i+1], array[high]) = (array[high], array[i+1])

        # Return the position from where partition is done
        return (i+1)

    def qsort(array, low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            p = partition(array, low, high)

            # Recursive call on the left of pivot
            qsort(array,low, p-1)
            # Recursive call on the right of pivot
            qsort(array, p+1, high)

data = [2,5,1,9,4,10,15,12,-4,-3,20,28,8]
print("Before:")
print(data)

size = len(data)

quicksort(data,0,size-1)

print("After:")
print(data)