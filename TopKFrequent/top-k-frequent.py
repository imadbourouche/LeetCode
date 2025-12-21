from typing import List

# # Naive approach using sorting frequency map - O(n log n)
# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     frequency_map = {}
#     for i in nums: # O(n)
#         frequency_map[i] = frequency_map.get(i, 0) + 1
#     sorted_items = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True) # O(m log m) where m is the number of unique elements
#     return [key for key, value in sorted_items[:k]]  # O(k)

# Optimized approach using bucket sort - O(n)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequency_map = {}
    reverse_frequency_map = {}
    max_frequency = 0
    # build frequency map
    for i in nums:
        frequency_map[i] = frequency_map.get(i, 0) + 1

    # build reverse frequency map
    for num, frequency in frequency_map.items():
        reverse_frequency_map.setdefault(frequency, set()).add(num)
        if frequency > max_frequency:
            max_frequency = frequency
    result = set()
    while k > 0:
        bucket = reverse_frequency_map.get(max_frequency, set())
        for num in bucket:
            if k == 0:
                break
            result.add(num)
            k -= 1
        max_frequency -= 1
    return list(result)