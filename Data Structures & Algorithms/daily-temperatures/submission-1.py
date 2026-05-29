class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = [] #pair(i,temp)
        for idx,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:# Checking if Stack exists and if current temp is greater than prev temp
                stackI, stackT = stack.pop() # Storing the value of popped idx and temp
                res[stackI] = idx-stackI # Appending the difference of the idexes to res
            stack.append((idx,temp)) # Adding the index and temp of the next least temp
        return res

        