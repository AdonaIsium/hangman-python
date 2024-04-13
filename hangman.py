# This will be an application which will allow the user to play a game of hangman.

# Importing the random module
import random

# Create Word List
word_list = ["apple", "game", "Hollywood", "spectrum", "associate", "hangman", "python", "jumble", "easy", "difficult", "answer", "xylophone", "storm", "light", "apex", "crazy", "jazz", "buzz", "fizz", "puzzle", "oxygen", "pajamas", "yacht", "vodka", "zombie", "jigsaw", "jinx", "jackpot", "jogging", "jockey", "jewel", "squirrel", "jungle", "jumper", "tiger", "elephant", "rhino", "giraffe", "zebra", "lion", "cheetah", "leopard", "panther", "puma", "cougar", "lynx", "bobcat", "tiger", "jaguar", "ocelot", "snow", "ice", "frost", "freeze", "cold", "chill", "polar", "arctic", "antarctic", "glacier", "avalanche", "blizzard", "hail", "sleet", "slush", "frostbite", "hypothermia", "igloo", "iceberg", "frozen", "snowman", "snowball", "snowflake", "snowstorm", "snowdrift", "snowplow", "snowmobile", "snowshoe", "snowboard", "ski", "skate", "sled", "sleigh", "frosty", "chilly", "icy", "slippery", "white", "winter", "cold", "frost", "freeze", "snowy", "icy", "chill", "blizzard", "polar", "arctic", "antarctic", "glacier", "avalanche", "hail", "sleet", "slush", "frostbite", "hypothermia", "igloo", "iceberg", "frozen", "snowman", "snowball", "fire", "flame", "heat", "burn", "hot", "warm", "blaze", "inferno", "embers", "smoke", "ash", "charcoal", "coal", "soot", "fireplace", "campfire", "bonfire", "barbecue", "grill", "stove", "oven", "furnace", "heater", "firefighter", "fireproof", "firewood", "firecracker", "firefly", "firestorm", "firetruck", "fireman", "firehouse", "firehose", "firebrand", "fireball", "fireplace", "firework", "firearm", "fireproof", "firefighter", "golf", "soccer", "football", "basketball", "starcraft", "vertex", "thermal", "dynamic", "static", "kinetic", "potential", "energy", "force", "gravity", "acceleration", "velocity", "speed", "distance", "time", "mass", "weight", "astronomy", "planet", "star", "galaxy", "universe", "cosmos", "blackhole", "nebula", "supernova", "quasar", "pulsar", "comet", "asteroid", "meteor", "meteorite", "moon", "sun", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "mercury", "venus", "asteroid", "meteoroid", "meteorite", "comet", "moon", "sun", "star", "galaxy", "universe", "cosmos", "blackhole", "nebula", "supernova", "quasar", "pulsar", "planet", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "mercury", "venus", "asteroid", "meteoroid", "meteorite", "comet", "moon", "sun", "star", "galaxy", "universe", "cosmos", "blackhole", "nebula", "supernova", "quasar", "pulsar", "planet", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "mercury", "venus", "asteroid", "meteoroid", "meteorite", "comet", "moon", "sun", "star", "galaxy", "universe", "cosmos", "blackhole", "nebula", "supernova", "quasar", "pulsar", "planet", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "mercury", "venus", "asteroid", "meteoroid", "meteorite", "comet", "moon", "sun", "star", "galaxy", "universe", "cosmos", "blackhole", "nebula", "supernova", "quasar", "pulsar", "planet", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "mercury", "venus", "asteroid", "meteoroid", "meteorite", "comet", "moon", "sun", "star", "mario", "pikachu", "link", "zelda", "werebear", "sword", "knight", "mage", "thief", "dagger", "gold", "lute"]

# Define Functions:
def choose_word():
    return random.choice(word_list)

def initialize_letters_of_word(letters_of_word, chosen_word):
    for i in range(0, len(chosen_word)):
        letters_of_word.append("_")
    return letters_of_word

def get_guess(chosen_word, lives, letters_of_word):
    new_lives = lives
    new_letters_of_word = letters_of_word
    guess = input("\n Guess a letter: ").lower()
    if guess in chosen_word:
        for i in range(0, len(chosen_word)):
            if guess == chosen_word[i]:
                new_letters_of_word[i] = guess
                print(new_letters_of_word[i], end="")
            else:
                print(new_letters_of_word[i], end="")
    else:
        print("Incorrect guess. Try again.")
        new_lives -= 1
    return new_lives, new_letters_of_word


def game():
    chosen_word = choose_word()
    letters_of_word = []
    initialize_letters_of_word(letters_of_word, chosen_word)
    lives = 6
    while lives > 0:
        if "_" not in letters_of_word:
            print("You win!")
            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again == "yes":
                game()
            break
        lives, letters_of_word = get_guess(chosen_word, lives, letters_of_word)
        print(lives)
        print(letters_of_word)

if __name__ == "__main__":
    game()

