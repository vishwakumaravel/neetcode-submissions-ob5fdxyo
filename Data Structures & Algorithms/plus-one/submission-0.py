class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stri = "".join(str(x) for x in digits)
        final_num = 1 + int(stri)
        strn = str(final_num)
        final_list = []
        for s in strn:
            final_list.append(s)
        return final_list
        