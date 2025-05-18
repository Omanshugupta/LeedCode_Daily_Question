from itertools import product

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [0, 1, 2]  # Red, Green, Blue
        valid_cols = []
        def is_valid(col):
            return all(col[i] != col[i+1] for i in range(len(col)-1))

        for col in product(colors, repeat=m):
            if is_valid(col):
                valid_cols.append(col)
        neighbors = {}
        for col1 in valid_cols:
            neighbors[col1] = []
            for col2 in valid_cols:
                if all(col1[i] != col2[i] for i in range(m)):
                    neighbors[col1].append(col2)

        dp = {col: 1 for col in valid_cols}

        for _ in range(1, n):
            new_dp = {col: 0 for col in valid_cols}
            for col1 in valid_cols:
                for col2 in neighbors[col1]:
                    new_dp[col2] = (new_dp[col2] + dp[col1]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
