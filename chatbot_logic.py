# chatbot_logic.py
import re
import random

genres = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator", "The Dark Knight", "Avengers: Endgame"],
    "comedy": ["The Hangover", "Superbad", "Step Brothers", "Monty Python and the Holy Grail", "Dumb and Dumber", "Bridesmaids"],
    "horror": ["The Conjuring", "Hereditary", "Get Out", "It", "A Quiet Place", "The Exorcist"],
    "sci-fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049", "Dune", "Arrival"],
    "romance": ["The Notebook", "La La Land", "Pride & Prejudice", "Titanic", "Crazy Rich Asians", "Me Before You"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather", "Schindler's List", "Green Book", "A Beautiful Mind"],
    "fantasy": ["The Lord of the Rings", "Harry Potter", "The Hobbit", "Pan's Labyrinth", "The Shape of Water", "Stardust"],
    "thriller": ["Se7en", "Gone Girl", "Shutter Island", "Prisoners", "The Girl with the Dragon Tattoo", "No Country for Old Men"],
    "animation": ["Toy Story", "Shrek", "Spirited Away", "Coco", "Frozen", "How to Train Your Dragon"],
    "documentary": ["The Social Dilemma", "13th", "Won't You Be My Neighbor?", "Free Solo", "Making a Murderer", "Our Planet"]
}

responses = [
    (r"(.*)recommend(.*)", "Of course! What genre are you interested in? We have action, comedy, horror, sci-fi, romance, drama, fantasy, thriller, animation, and documentary."),
    (r"(.*)action(.*)", lambda: f"You might enjoy {random.choice(genres['action'])}. Do you have a favorite actor or director?"),
    (r"(.*)comedy(.*)", lambda: f"Here are some laughs: {random.choice(genres['comedy'])}. What's your go-to comedy style?"),
    (r"(.*)horror(.*)", lambda: f"These might give you chills: {random.choice(genres['horror'])}. Do you prefer supernatural or psychological horror?"),
    (r"(.*)sci[- ]?fi(.*)", lambda: f"Try this futuristic adventure: {random.choice(genres['sci-fi'])}. Are you into space or dystopian futures?"),
    (r"(.*)romance(.*)", lambda: f"Love is in the air with: {random.choice(genres['romance'])}. Do you like classic or modern romance films?"),
    (r"(.*)drama(.*)", lambda: f"Get ready for an emotional ride with: {random.choice(genres['drama'])}. Do you enjoy historical or contemporary dramas?"),
    (r"(.*)fantasy(.*)", lambda: f"Escape into a magical world with: {random.choice(genres['fantasy'])}. What's your favorite fantasy universe?"),
    (r"(.*)thriller(.*)", lambda: f"This will keep you on the edge of your seat: {random.choice(genres['thriller'])}. Do you prefer crime or psychological thrillers?"),
    (r"(.*)animation(.*)", lambda: f"Animation lovers, here you go: {random.choice(genres['animation'])}. Do you like Western or Japanese animation more?"),
    (r"(.*)documentary(.*)", lambda: f"Expand your knowledge with: {random.choice(genres['documentary'])}. Any specific topic you're interested in?"),
    (r"(.*)yes(.*)", "Great! I'm glad you're excited. What genre would you like recommendations for?"),
    (r"(.*)hi|hello(.*)", "Hi there! I'm your movie recommendation assistant. What genre are you in the mood for today?"),
    (r"(.*)thank(.*)", "You're welcome! Enjoy your movie! If you need more suggestions, just ask!"),
    (r"(.*)bye(.*)", "Goodbye! Happy watching! Come back anytime for more movie recommendations!"),
    (r"(.*)", "I'm not sure I understand. Can you tell me what genre you're interested in or ask for recommendations?")
]

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in responses:
        if re.match(pattern, user_input):
            return response() if callable(response) else response
    return "I'm not sure I understand. Please try again."
