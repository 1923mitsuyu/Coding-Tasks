# Point: Sort the array and compare the first and the last value in the array
# Point: With min() function, the smaller value, which is set as the length of the loop, is chosen

class Solution:
    def longestCommonPrefix(strs):

        output = ""
        strs = sorted(strs)
        
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if(strs[0][i] == strs[-1][i]): output += strs[0][i]
            else: return output 

        return output 

