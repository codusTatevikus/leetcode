class Solution:
    def reverse_num(self, num):
        reverse_n = 0
        while num:
            reverse_n = reverse_n * 10 + num % 10
            num //= 10
        return reverse_n

    def isSameAfterReversals(self, num: int) -> bool:
        cnum = num
        rnum = self.reverse_num(num)
        rnum1 = self.reverse_num(rnum)
        return rnum1 == cnum