
movies = {
    "Titanic": ["Romance", "Drama"],
    "The Avengers": ["Action", "Adventure", "Sci-Fi"],
    "The Notebook": ["Romance", "Drama"],
    "Iron Man": ["Action", "Sci-Fi"],
    "Inception": ["Action", "Sci-Fi", "Thriller"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Dark Knight": ["Action", "Thriller"],
    "La La Land": ["Romance", "Musical", "Drama"],
    "Doctor Strange": ["Action", "Fantasy", "Sci-Fi"],
    "The Fault in Our Stars": ["Romance", "Drama"]
}

# Function to recommend movies based on shared genres
def recommend(movie_name):
    if movie_name not in movies:
        return ["Movie not found in database!"]

    target_genres = set(movies[movie_name])
    similarity_scores = {}

    for other_movie, genres in movies.items():
        if other_movie == movie_name:
            continue
        # Count matching genres
        score = len(target_genres.intersection(genres))
        similarity_scores[other_movie] = score

    # Sort movies by similarity score (high → low)
    sorted_movies = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    # Pick top 5 with at least 1 matching genre
    recommended = [movie for movie, score in sorted_movies if score > 0][:5]
    return recommended if recommended else ["No similar movies found!"]

# -------------------------
# Main Program
print("Simple Movie Recommendation System")
print("==================================")

# Ask user input (or default = Titanic if left empty)
user_input = input("Enter a movie you like (or press Enter to test with Titanic): ")

if user_input.strip() == "":
    user_input = "Titanic"

recommendations = recommend(user_input)

print(f"\nRecommended Movies for You (based on '{user_input}'):")
for i, movie in enumerate(recommendations, start=1):
    print(f"{i}. {movie}")



