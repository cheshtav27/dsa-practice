class Solution:
    def canConstruct(self, ransomNote, magazine):
        frequency = {}

        for char in magazine:
            frequency[char] = frequency.get(char, 0) + 1

        for char in ransomNote:
            if char not in frequency:
                return False

            if frequency[char] == 0:
                return False

            frequency[char] -= 1

        return True