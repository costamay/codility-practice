def solution(skills):
    n = len(skills)
    results = {player: 1 for player in range(n)}
    c_round = 1
    c_matches = [player for player in range(n)]
    while len(c_matches) > 1:
        n_matches = []
        i = 0
        while i < len(c_matches) - 1:
            p1, p2 = c_matches[i], c_matches[i + 1]
            winner = max(p1, p2, key=lambda x: skills[x])
            loser = min(p1, p2, key=lambda x: skills[x])
            n_matches.append(winner)
            results[loser] = c_round
            i += 2
        c_matches = n_matches
        if len(c_matches) > 1:
            c_round += 1
    winner = c_matches[0]
    results[winner] = c_round
    return list(results.values())