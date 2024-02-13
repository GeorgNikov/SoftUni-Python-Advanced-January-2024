def team_lineup(*players):
    result = {}

    for player_name, country in players:
        result.setdefault(country, []).append(player_name)

    sorted_result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x)))
    final_result = []

    for key, value in sorted_result.items():
        final_result.append(f"{key}:")
        final_result.extend([f"  -{obj}" for obj in value])

    return "\n".join(final_result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print()
print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print()
print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
