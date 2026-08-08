class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        seen = {0: 1}

        for num in nums:
            prefix_sum += num

            required = prefix_sum - k

            if required in seen:
                count += seen[required]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count