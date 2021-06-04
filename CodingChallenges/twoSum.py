'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Runtime: 3872 ms, faster than 5.75% of Python online submissions for Two Sum.
Memory Usage: 14.3 MB, less than 23.18% of Python online submissions for Two Sum.
'''
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))


main()
