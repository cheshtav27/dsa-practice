class Solution:
    def topKFrequent(self, nums, k):
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in frequency.items():
            buckets[count].append(num)

        result = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result