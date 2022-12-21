class Solution:
    def twoCitySchedCost(self, costs):
        element = len(costs)//2
        ans = 0
        d, fb = [], []
        for cost in costs:
            if cost[0] < cost[1]:
                ans += cost[0]
                fb.append(cost[1]-cost[0])
            else:
                ans += cost[1]
                d.append(cost[0]-cost[1])

        if len(d) < len(fb):
            fb.sort()
            for j in range(len(fb)-element):
                ans += fb[j]

        if len(d) > len(fb):
            d.sort()
            for i in range(len(d)-element):
                ans += d[i]

        return ans
