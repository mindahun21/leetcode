class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        count = defaultdict(list)
        res = []

        for access in access_times:
            time = int(access[1][:2])*60 + int(access[1][2:])
            count[access[0]].append(time)

            if len(count[access[0]]) >=3:
                acs =  sorted(count[access[0]])

                l=0
                for r in range(2,len(acs)):
                    if acs[r] - acs[l] < 60 and access[0] not in res:
                        res.append(access[0])
                        break
                    l+=1


        return res