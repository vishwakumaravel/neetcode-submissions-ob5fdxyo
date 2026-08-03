class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for x in details:
            if int(str(x[11:13])) > 60:
                cnt +=1
        return cnt