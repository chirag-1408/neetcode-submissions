class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = [] #pair(i,temp)
        for idx,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackI, stackT = stack.pop()
                res[stackI] = idx-stackI
            stack.append((idx,temp))
        return res

        