"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one 
of these people is secretly the town judge.

If the town judge exists, then:

    * The town judge trusts nobody.
    * Everybody (except for the town judge) trusts the town judge.
    * There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the 
person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town 
judge.  Otherwise, return -1.
"""

class TownJudge(object):

    def find_judge(self, N, trust):
        """Finds town judge as per problem description.

        Args:
            N: number of people ranging from 1 to N.
            trust: List[List[int]] List of element pairs [a,b] implying that
                a trusts b.

        Returns:
            Returns int representing label of judge if he exists, else returns
            -1.
        """
        if not trust:
            assert N == 1; return N
        trust_map = {k:set() for k in range(1, N+1)}
        for trust_pair in trust:
            a,b = trust_pair
            trust_map[a].add(b)
        # Find persons that trust nobody
        trust_nobody = set()
        for k,v in trust_map.items():
            if not v: trust_nobody.add(k)
        print(trust_map)
        # Finds trust_nobody persons that are trusted by everybody
        # We loop through all the keys in our trust map and try to find
        # the one person who is in all of their values.
        for k,v in trust_map.items():
            # Avoid trust maps of people who trust nobody as they are empty.
            if k in trust_nobody: continue
            common = trust_nobody.intersection(v)
            if not common: break
            if len(common) < 2: return common.pop()
            trust_nobody = common
        return -1

tj = TownJudge()
assert tj.find_judge(1, []) == 1
assert tj.find_judge(2, [[2,1]]) == 1
assert tj.find_judge(2, [[1,2]]) == 2
assert tj.find_judge(3, [[1,3], [2,3]]) == 3
assert tj.find_judge(3, [[1,3], [2,3], [3,1]]) == -1
assert tj.find_judge(3, [[1,2],[2,3]]) == -1
assert tj.find_judge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3