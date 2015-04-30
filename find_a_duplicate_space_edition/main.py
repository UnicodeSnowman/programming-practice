import random

def generate_nums(n):
    nums = []
    for num in range(n + 1):
        nums.append(random.randrange(1, n + 1))

    return nums

# O(n) time
# O(n) space
def find_dups_one(nums):
    found_values = {}

    for num in nums:
        if num in found_values:
            return num
        else:
            found_values[num] = True

# O(n^2) time
# O(1) space
def find_dups_two(nums):
    for val in range(1, len(nums)):
        seen = False
        for num in nums:
            if num == val:
                if seen == True:
                    return num
                else:
                    seen = True

# O(nlogn) time, from sort... actually nlogn + n, but that term ignored
# O(1) space (if in-place sort, i.e. in-place merge sort)
def find_dups_three(nums):
    # pretend this is in-place sort,
    # which (unfortunately) mutates the input
    sorted_nums = sorted(nums) # nlogn?
    val = 0
    for num in sorted_nums:
        if val == num:
            return num
        else:
           val = num

# O(nlogn)
# O(1), w/o mutating input array
def find_dups_four(nums):
    left = len(nums)/2
 
    print(sorted(nums))
    print(left_count, right_count)

def iter(nums):
    half = len(nums)/2
    left_count = 0
    right_count = 0
    for num in nums:
        if num < half:
            left_count = left_count + 1
        if num >= half:
            right_count = right_count + 1

    return left_count if left_count > right_count else right_count

#res = find_dups_one(generate_nums(5))
#res = find_dups_two(generate_nums(5))
#res = find_dups_three(generate_nums(15))
res = find_dups_four(generate_nums(10))
print(res)
