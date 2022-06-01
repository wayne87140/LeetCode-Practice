# My Code
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        last_char=''
        id = {'':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        for index, char in enumerate(s):
            if id.get(last_char+char):
                result = result - id.get(last_char) + id[last_char+char]
            else:
                result += id[char]
            last_char = char
              
        return result

'''
LeetCode
class Solution:
# @param {string} s
# @return {integer}
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]
'''