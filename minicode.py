import spacy
import datetime
import random

# load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# define a function to get the user's mood
def get_mood():
    mood = input("\nHow are you feeling today? ")
    return mood

# define a function to save the user's mood data to a file
def save_data(mood):
    today = datetime.date.today()
    filename = "mental_fitness_tracker.txt"
    with open(filename, "a") as f:
        f.write(f"{today}: Mood: {mood}\n")

# define a function to display a suggestion based on the user's mood
def display_suggestion(mood):
    suggestions = {
        "happy": "Great to hear! Keep doing what you're doing!",
        "sad": "I'm sorry to hear that. Try to do something that makes you happy, like listening to music or spending time with loved ones.",
        "stressed": "That can be tough. Take a break and do something relaxing, like reading a book or going for a walk.",
        "anxious": "I understand how you feel. Try some deep breathing exercises or meditation to help calm your mind.",
        "tired": "I hear you. Try to get some rest and prioritize self-care today.",
        "motivated": "Awesome! Keep up the great work!",
        "unmotivated": "It's okay to feel unmotivated sometimes. Try breaking your tasks into smaller, more manageable ones to help you get started.",
        "overwhelmed": "That can be tough. Make a list of your tasks and prioritize what needs to be done first.",
        "bored": "I see. Try picking up a new hobby or doing something you enjoy to help you feel more engaged.",
        "angry": "I'm sorry to hear that. Try some deep breathing exercises or going for a run to release some of that tension.",
    }
    if mood in suggestions:
        return suggestions[mood]
    else:
        return "\nI'm not sure what to suggest. Try doing something that usually makes you happy or relaxed."

# define a function to generate a response based on user input
def generate_response(input_text):
    # create a spaCy Doc object from the user input
    input_doc = nlp(input_text.lower())
    # check if the user wants to track their mood for today
    if "track" in input_text and "mood" in input_text:
        mood = get_mood()
        save_data(mood)
        return display_suggestion(mood)
    # provide some general tips for mental fitness
    elif "tips" in input_text or "advice" in input_text:
        return "\nHere are some general tips for maintaining good mental health: get enough sleep, exercise regularly, eat a healthy diet, stay hydrated, practice relaxation techniques such as meditation or deep breathing, and seek professional help if needed."
    # if none of the above conditions are met, provide a default response
    else:
        return "\nI'm sorry, I didn't understand. Can you please try again?"

# define the main function to run the mental fitness tracker chatbot
def main():
    print("Welcome to the mental fitness tracker chatbot!")
    while True:
        user_input = input("\nHow can I assist you today? ")
        response = generate_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
