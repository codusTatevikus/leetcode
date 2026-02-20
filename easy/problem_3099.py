class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        cx = x
        sumx = 0

        while cx:
            sumx += cx % 10
            cx //= 10

        if x % sumx == 0:
            return sumx
        return -1