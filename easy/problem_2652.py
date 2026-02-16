class Solution:
    def sumOfMultiples(self, n: int) -> int:
        answer = 0
        i = 1
        while i <= n:
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                answer += i
            i += 1
        return answer