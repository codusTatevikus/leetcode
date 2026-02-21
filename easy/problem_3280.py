class Solution:
    def convertDateToBinary(self, date: str) -> str:
        answer = []
        for i in date.split('-'):
            answer.append(format(int(i), 'b'))
        result = "-".join(answer)
        return result