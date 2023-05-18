def climbingLeaderboard(ranked, player):

    scores = sorted(list(set(ranked)), reverse=True)
    player_rank = []

    for score in player:
        while scores and score >= scores[-1]:
            scores.pop()
        player_rank.append(len(scores) + 1)

    return player_rank


rank = [100, 90, 90, 80]
players = [70, 80, 105]
print(climbingLeaderboard(rank, players))
