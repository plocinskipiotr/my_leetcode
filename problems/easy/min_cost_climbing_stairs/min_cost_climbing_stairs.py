from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            short_step_cost = cost[i] + cost[i + 1]
            long_step_cost = cost[i] + cost[i + 2]
            cost[i] = min(short_step_cost, long_step_cost)

        return min(cost[0], cost[1])
