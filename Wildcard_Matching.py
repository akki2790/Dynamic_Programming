# 44. Wildcard Matching

#Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#
#    '?' Matches any single character.
#    '*' Matches any sequence of characters (including the empty sequence).
#
#The matching should cover the entire input string (not partial).
#
#Recursion with Memoization
#
#If the strings are equal (p == s), then return True.
#If the pattern matches any string (p == '*'), then return True.
#If p is empty, or s is empty, return False.
#If the current characters match (p[0] == s[0] or p[0] == '?'), then compare the next ones and return isMatch(s[1:], p[1:]).
#If the current pattern character is a star (p[0] == '*'), then there are two possible situations:
#    The star matches no characters, and hence the answer is isMatch(s, p[1:]).
#    The star matches one or more characters, and so the answer is isMatch(s[1:], p).
#If p[0] != s[0], return False.
#
#Note: There' the edge case where the pattern might have consecutive. You'll have to remove those first.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def rm_dup_star(pattern):
            px = []
            for i in range(len(pattern)):
                if px == []:
                    px.append(pattern[i])
                elif px[-1] == "*" and pattern[i] == "*":
                    continue
                else:
                    px.append(pattern[i])
            return "".join(px)
        print (rm_dup_star(p))
        
        def match(s,p): # recurssive
            if (s,p) in dp:
                return dp[(s,p)]
            if s == p or p == "*":
                dp[(s,p)] = True
            elif s == "" or p == "":
                dp[(s,p)] = False
            elif s[0] == p[0] or p[0] == "?":
                dp[(s,p)] = match(s[1:],p[1:])
            elif p[0] == "*":
                dp[(s,p)] = match(s,p[1:]) or  match(s[1:],p)
            else:
                dp[(s,p)] = False
            return dp[(s,p)]
        
        dp = defaultdict(bool)
        p = rm_dup_star(p)
        return match(s,p)
