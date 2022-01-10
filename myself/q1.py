# ## Problem - Rotated Lists

# We'll solve the following problem step-by-step:

# > You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
#  Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list.
# You can assume that all the numbers in the list are unique.
# > Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.
# > We define "rotating a list" as removing the last element of the list and adding it before the first element. 
# E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`. 
# >"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
# >

## The Method

# Here's the systematic strategy we'll apply for solving problems:

# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

# This approach is explained in detail in [Lesson 1](https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-1-binary-search-linked-lists-and-complexity) of the course. Let's apply this approach step-by-step.


# a sorted list is rotated so find min no. of times it has been rotated
# [1,2,3,4,5] is the sorted list
# input:[4,5,1,2,3]
# output:2
#*********EDGE CASES**************
# 1. list is rotated
# 2. lsit is unrotated
# 3. list is empty
# 4. list has 1 element
# 5. list is rotated len-1 times

test1={
    "input":{
        "nums":[3,4,5,1,2]
    },
    "output":3
}


test2={
    "input":{
        "nums":[2,3,4,5,1]
    },
    "output":4
}

test3={
    "input":{
        "nums":[]
    },
    "output":0
}


test4={
    "input":{
        "nums":[1]
    },
    "output":0
}

test5={
    "input":{
        "nums":[1,2,3,4,5]
    },
    "output":0
}

def min_rotat(arr):
    print(arr)
    if len(arr)==0:
        return 0
    for i in range(len(arr)):
        if i !=len(arr)-1 and arr[i]>arr[i+1]:
            return i+1
    return 0

print(min_rotat(test1['input']['nums']))
print(min_rotat(test2['input']['nums']))
print(min_rotat(test3['input']['nums']))
print(min_rotat(test4['input']['nums']))
print(min_rotat(test5['input']['nums']))

# print(test1["input"])