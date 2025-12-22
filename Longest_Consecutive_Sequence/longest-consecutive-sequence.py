
from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    # Using a set to track numbers for O(1) lookups
    set_nums = set(nums)
    longest_sequence = 1

    # Iterate through each number in the list
    for i in nums:
        if i in set_nums:
            local_longest_sequence = 1
            set_nums.remove(i)

            # Explore lower numbers sequence
            tmp_back = i -1
            while tmp_back in set_nums:
                set_nums.remove(tmp_back)
                local_longest_sequence += 1
                tmp_back -= 1

            # Explore higher numbers sequence 
            tmp_front = i + 1
            while tmp_front in set_nums:
                set_nums.remove(tmp_front)
                local_longest_sequence += 1
                tmp_front += 1
        # Update the longest sequence found
        if local_longest_sequence > longest_sequence:
            longest_sequence = local_longest_sequence
    return longest_sequence

input = [1,1,0,1]
print(longestConsecutive(None, input))