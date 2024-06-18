from flask import Flask, render_template
import random
 
app = Flask(__name__)
 
# Lists of story elements
 
beginnings = ["Once upon a time", "In a land far away", 
              "In the not-so-distant future", 
              "Amidst the ruins of an ancient civilization", 
              "In the heart of a magical kingdom",
              "Underneath the starry night sky",
              "Upon the edge of the known universe"]

characters = ["a brave knight", "an adventure explorer", 
              "a curious scientist", "a mischievous wizard", 
              "a noble princess", "a cunning pirate",
              "a time-traveling adventurer", "a legendary hero",
              "a mysterious traveler", "a fearless warrior",
              "a wise old sage", "a spirited young apprentice"]

settings = ["a mysterious forest", "a bustling city", 
            "an ancient castle", "a hidden underground lair", 
            "a distant planet in a far-off galaxy", 
            "a sunken underwater city",
            "a majestic mountain peak", "a tranquil village",
            "an enchanted garden", "a haunted mansion",
            "a futuristic metropolis", "an otherworldly realm"]

conflicts = ["batlling a fearsome dragon", 
             "discovering a hidden treasure", 
             "solving a perplexing mystery", 
             "defending against an alien invasion", 
             "escaping from a labyrinthine maze", 
             "unraveling a curse that plagues the land",
             "confronting their inner demons", 
             "forging unlikely alliances", 
             "surviving a natural disaster", 
             "unlocking the secrets of an ancient prophecy",
             "challenging the gods themselves", 
             "escaping from a parallel dimension"]

endings = ["and they all lived happily ever after", 
           "and the world was forever changed", 
           "and they found their way back home.", 
           "but darkness still lurked on the horizon", 
           "and a new adventure awaited them", 
           "and they realized that the journey was just beginning",
           "and they discovered the true meaning of friendship",
           "and the power of love triumphed over all", 
           "and they returned as legends of their time", 
           "but their greatest adventure was yet to come",
           "and they became the stuff of legends", 
           "and the stars themselves bowed to their greatness"]

def generate_story():
    beginning = random.choice(beginnings)
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    ending = random.choice(endings)

    # Additional descriptive elements, character interactions, and plot developments
    intro = f"{beginning}. In a world where magic and mystery intertwine, {character} was known as a legend in their own right, \
a champion of justice and bravery. Their latest adventure led them to the fabled land of {setting}, a realm shrouded in \
secrets and danger."

    journey = "As they embarked on their journey, they were joined by a band of companions, each with their own unique \
skills and backgrounds. Together, they traversed through {setting}, facing countless trials and tribulations along the way. \
From {conflict} to {random.choice(conflicts)}, their resolve was put to the test, but they remained undeterred."

    discovery = "Amidst the challenges, they made astonishing discoveries and forged unbreakable bonds. They encountered \
ancient ruins teeming with forgotten knowledge, encountered mystical creatures of legend, and unlocked the mysteries of the \
cosmos itself."

    climax = f"And as they reached the climax of their journey, facing their ultimate challenge in the form of {conflict}, \
they stood united against the forces of darkness, their courage shining brighter than any star in the sky."

    resolution = f"Finally, as the dust settled and the echoes of battle faded, {ending}. But their adventures were far from \
over, for wherever there was darkness, they would be there to bring light, wherever there was injustice, they would be there \
to deliver justice, for they were not just heroes, they were legends."

    # Combine all parts of the story
    story = "\n\n".join([intro, journey, discovery, climax, resolution])

    return story
 
# Define a route to generate and display a story
 
@app.route('/')
def index():
    story = generate_story()
    return render_template('./web_show.html', story=story)
 
if __name__ == '__main__':
    app.run(debug=True)