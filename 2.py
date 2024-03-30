# import math
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # 元の値をコピー
        original = x
        palindrome = 0

        while(x > 0):
            # 121 % 10 = 1のように抽出
            digit = x % 10
            # Tip: 10の位 / 100の位と上がるので10をかける
            palindrome = palindrome * 10 + digit
            # 12.1 => 12にするためにfloor関数を使用
            x = math.floor(x / 10)
        
        return original == palindrome

