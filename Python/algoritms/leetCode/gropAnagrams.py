import collections


def groupAnagrams(str):
    ans = collections.defaultdict(list)

    for s in str:
        count = [0] * 26
        for c in s:
            count[ord(c) -ord("a")] +=1
        ans[tuple(count)].append(s)
    return ans.values()