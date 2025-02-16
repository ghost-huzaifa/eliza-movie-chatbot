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
        (r'(hi|hello)', "Hello! I'm a movie recommendation chatbot. What kind of movie are you in the mood for today?"),
        (r'(.*)?recommend(.*)?', "Of course! What genre are you interested in? We have action, comedy, horror, sci-fi, romance, drama, fantasy, thriller, animation, and documentary."),
        (r'(.*)?action(.*)?',lambda: f"You might enjoy {random.choice(genres['action'])}. Do you want another recommendation?"),
        (r'(.*)?comedy(.*)?',lambda: f"{random.choice(genres['comedy'])} will make you laugh. Do you want another recommendation?"),
        (r'(.*)?horror(.*)?',lambda: f"This movie might give you chills: {random.choice(genres['horror'])}. Do you want another recommendation?"),
        (r'(.*)?sci[- ]?fi(.*)?',lambda: f"Try this futuristic adventure movie: {random.choice(genres['sci-fi'])}. Do you want another recommendation?"),
        (r'(.*)?romance(.*)?',lambda: f"Love is in the air with {random.choice(genres['romance'])}. Do you want another recommendation?"),
        (r'(.*)?drama(.*)?',lambda: f"Get ready for an emotional ride with: {random.choice(genres['drama'])}. Do you want another recommendation?"),
        (r'(.*)?fantasy(.*)?',lambda: f"Escape into these magical world with {random.choice(genres['fantasy'])}.  Do you want another recommendation?"),
        (r'(.*)?thriller(.*)?',lambda: f"This will keep you on the edge of your seat: {random.choice(genres['thriller'])}.  Do you want another recommendation?"),
        (r'(.*)?animation(.*)?',lambda: f"Animation lovers, here you go: {random.choice(genres['animation'])}.  Do you want another recommendation?"),
        (r'(.*)?documentary(.*)?',lambda: f"Expand your knowledge with this documentary: {random.choice(genres['documentary'])}.  Do you want another recommendation?"),
        (r'(.*)?thank(.*)?', "You're welcome! Enjoy your movie! If you need more suggestions, just ask!"),
        (r'(.*)?bye(.*)?', "Goodbye! Happy watching! Come back anytime for more movie recommendations!"),
        (r'(.*)', "I'm not sure I understand. Can you tell me what genre you're interested in or ask for recommendations?")
    ]

def elizaResponse(userInput):
    for (pattern, response) in responses:
        if (re.match(pattern, userInput.lower())):
            if callable(response):
                return response()
            else:
                return response
    return "I can't understand what you are saying, try saying again using proper words."

botName = "Ryan Gosling"
userName = input(f"{botName}: Hi! I'm {botName}, your movie recommendation chatbot, what's your name?\n")
print(f"{botName}: Hi! {userName}, nice to meet you!")

while(True):
    userInput = input(f"{userName}: ")
    if "bye" in userInput:
        print(f"{botName}: Goodbye! I hope you got some good movies to watch tonight!")
        break
    response = elizaResponse(userInput)
    print(f"{botName}: {response}")

    