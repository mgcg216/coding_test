from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                print(hash_table[i])
        print()
        return 0

if __name__ == "__main__":
    Solution.singleNumber()
