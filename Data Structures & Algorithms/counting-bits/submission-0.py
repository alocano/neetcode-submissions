class Solution:
    def countBits(self, n: int) -> List[int]:
        total = [0] * (n + 1)
        for i in range(1, n + 1):
            total[i] = total[i >> 1] + (i & 1)
        return total