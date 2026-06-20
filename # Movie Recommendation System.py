# Movie Recommendation System

movies = {
    "Action": ["KGF", "Pushpa", "John Wick"],
    "Comedy": ["Jathi Ratnalu", "F2", "Jumanji"],
    "Drama": ["Hi Nanna", "The Pursuit of Happyness", "Jersey"],
    "Horror": ["The Conjuring", "Annabelle", "Insidious"],
    "Sci-Fi": ["Interstellar", "Inception", "Avatar"]
}

print("=== Movie Recommendation System ===")
print("Available Genres:")
print("Action, Comedy, Drama, Horror, Sci-Fi")

genre = input("\nEnter your favorite genre: ")

if genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Sorry! Genre not found.")