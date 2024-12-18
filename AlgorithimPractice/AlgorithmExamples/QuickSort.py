def quicksort(arr):

    def partition(low, high):
        i = low -1
        pval = arr[high]
        for j in range(low, high):  # from low to high -1
            if arr[j] < pval:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]
            arr[i+1], arr[high] = arr[high],arr[i+1]
        return i+1

    def qsort(low, high):
        if (low < high):
            pivot = partition(low,high)
            qsort(low,pivot-1)
            qsort(pivot+1,high)
    qsort(0,len(arr)-1)
##################################################


arr = [2,5,1,9,4,10,15,12,-4,-3,20,28,8]
print("Before Sorting:")
print(arr)

quicksort(arr)
print("After sorting:")
print(arr)
