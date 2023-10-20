def solution(s: str) -> str:
    if len(s) == 2:
        return s[0]
    map = {}
    for i in s:
        if i in map:
            map[i] = map[i] + 1
        else:
            map[i] = 0

    for i, v in map.items():

        if v <= 0:
            return i

    return "_"


print(solution("abacabad"))


def solucion2(s: str) -> str:
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'
