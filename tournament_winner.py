def tournamentWinner(competitions, results):
    # Write your code here.
    team_and_scores = {}
    
    for competition in competitions:
        team_and_scores[competition[0]] = 0
        team_and_scores[competition[1]] = 0
    
    for index_result in range(len(results)):
        if results[index_result] == 0:
            winning_team = competitions[index_result][1]
        else:
            winning_team = competitions[index_result][0]
        team_and_scores.update({winning_team : team_and_scores[winning_team]+3})
    
    print(team_and_scores.items())

    max_key = max(team_and_scores, key=team_and_scores.get)
    print(team_and_scores.get(max_key),max_key)
    return max_key    
    

def main():
    
    competitions= [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]

    
    print(tournamentWinner(competitions, results))


if __name__ == "__main__":
    main()