import collections
import re

class str_info:

    def palindrome(self,s:str) -> bool:
        strs = collections.deque()
        for char in s:
            strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    def slicing(self,s:str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

test_slising = str_info()
test = test_slising.palindrome('seungbinnibgnue')
print(test)
sli = test_slising.slicing('seungbinnibgnue')
print(sli)