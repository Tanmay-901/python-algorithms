# write a program to find all the pairs of integers whose sum is equal to a given number

# Things to ask the interviewer before solving
# does array contains only positive ints?
# what if same pair is repeated twice, should we print it again?
# if the reverse pair is acceptable for ex- (4,1) and (1,4) for given sum 5?
# Do we need to print only distinct pairs? is (3,3) is a valid pair for given sum 6?
# How big is the array?


def findpairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:  # don't print for same values
                continue
            if nums[i] + nums[j] == target:
                print(i, j)


# arr = [2, 6, 3, 9, 11]
arr = [1, 2, 3, 2, 3, 4, 5, 6]
findpairs(arr, 6)
