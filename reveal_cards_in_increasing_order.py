from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0] * n
        indices = deque(range(n))

        for card in sorted(deck):
            result[indices.popleft()] = card
            if indices:
                indices.append(indices.popleft())

        return result