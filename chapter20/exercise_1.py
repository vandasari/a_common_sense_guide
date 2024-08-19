"""
Exercise 1
"""


def players(basketball_players, football_players):
    ht_basketball = {}
    players_in_both_sports = []

    for player in basketball_players:
        ht_basketball[player["first_name"] + player["last_name"]] = player["team"]

    for p in football_players:
        if ht_basketball.get(p["first_name"] + p["last_name"]) is not None:
            players_in_both_sports.append(f"{p['first_name']} {p['last_name']}")

    return players_in_both_sports


if __name__ == "__main__":

    basketball_players = [
        {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
        {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
        {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
        {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
        {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"},
    ]

    football_players = [
        {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
        {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
        {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
        {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
        {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"},
    ]

    print(players(basketball_players, football_players))
