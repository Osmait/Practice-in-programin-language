def solution(words, ord):
    order_map = {}
    for i in range(0, len(ord)):
        order_map[ord[i]] = i
    for i in range(1, len(words)):
        if not comparation(words[i - 1], words[1], order_map):
            return False
    return True


def comparation(word1, word2, order_map):
    long = min(len(word1), len(word2))

    for i in range(0, long):
        if order_map[word1[i]] < order_map[word2[i]]:
            return True
        if order_map[word1[i]] > order_map[word2[i]]:
            return False
    return len(word1) <= len(word2)


words1 = ["habito", "hacer", "lectura", "sonreir"]
order1 = "hlabcedfgijkmnopqrstuvwxyz"
print(solution(words1, order1))
