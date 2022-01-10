# Binary Search Implementation
# Given a sorted array which can have repeated elemnts find the number given
# Edge Cases : 1. one element 2. 0 element 3. 
#assuming list is ascendingly sorted

#!!!!!!!!!!!!!!!!!!______________+++++++++++++++))))))))))(((((((((((((((((((((((((((<<<)))))))))))))))))))))))))))


# The Method 
# Here's the systematic strategy we'll apply for solving problems:
# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.


#!!!!!!!!!!!!!!!!!!______________+++++++++++++++))))))))))(((((((((((((((((((((((((((<<<)))))))))))))))))))))))))))


def binarySearch(array,number):
    print("inside bianry search")
    low = 0
    hi=len(array)-1
    mid = (low+hi)//2

    if(len(array))==0:
        return -1
    while low<=hi:
        mid = (low+hi)//2

        if number==array[mid]:
            print("found the")
            return mid
        elif number<array[mid]:
            hi =mid-1
        elif number>array[mid]:
            low = mid+1
    return -1

# print(binarySearch([1,2,3,4,5,7,7,7,8],7))

# def raised():
#     raise Exception('hello')

# raised()

# Define insertion sort in plane english and determine the space and time complexity of it
def insertion_sort(nums):
    nums = list(nums)
            # loop it for the lenght of list times
    for i in range(len(nums)):
# remove and save the last elemmtn into a variable 
        cur = nums.pop(i)
        # as the list got smaller now we have to iterate len(list)-1 number of times
        j = i-1
        # now we loop in the list from backward abd compare the numbers to the number we popped out
        while j >=0 and nums[j] > cur:
            j -= 1
        #and insert the number wehre the it is less than the number we popped
        nums.insert(j+1, cur)
    # atlast return the sorted array
    return nums            




    #Lets Implement Quick Sort
# Quikc Sort in Plain Englis :  Select a number at the end and implement partition function on it again run quicksort on partiontioned  array s in quick srot
# so the numbers in right of the pivot should be greater than the pivot and vice versa

def quickSort(nums,start=0,end=None):
    if end is None:
        nums=list(nums)
        end = len(nums)-1

    if start<end:
        pivot = partition(nums,start,end)
        quickSort(nums,start,pivot-1)
        quickSort(nums,pivot+1,end)

    return nums

# Lets see how partiotion happens: 
def partition(nums,start, end):
    # 2 indexes should be set to move elements here  and thre
    if end is None:
        end = len(nums)-1
    l,r=start,end-1
    while l<r:
        if nums[l]<=nums[end]:
            l+=1
        elif nums[r]>nums[end]:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]
    if nums[l]>nums[end]:
        nums[l],nums[end]= nums[end],nums[l]
        return l
    else:
        return end





























