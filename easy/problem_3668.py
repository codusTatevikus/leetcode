class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        for orde in order:
            if orde in friends:
                result.append(orde)
        return result