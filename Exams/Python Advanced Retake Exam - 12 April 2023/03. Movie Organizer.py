def movie_organizer(*movies):
    result = {}

    for movie_name, genre in movies:
        result.setdefault(genre, []).append(movie_name)

    #  Sorted in ascending order (alphabetically) by the movie's name
    sorted_values = {key: sorted(value) for key, value in result.items()}
    #  Sort the movies by the number of movies after that sorted ascending order (alphabetically) by genre.
    sorted_result = dict(sorted(sorted_values.items(), key=lambda x: (-len(x[1]), x)))

    final_result = []

    for key, value in sorted_result.items():
        final_result.append(f"{key} - {len(value)}")
        final_result.extend([f"* {obj}" for obj in value])

    return "\n".join(final_result)



print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))